from reportlab.pdfgen import canvas
from reportlab.graphics.barcode import code128, code39, code93, usps
from reportlab.graphics.barcode import qr, usps4s
from reportlab.graphics.shapes import Drawing
from reportlab.graphics import renderPDF
import re
import time
import win32api
import win32print
import os


def createBarCodes(c, barcode_value):
    # 条码生成
    barcode128 = code128.Code128(barcode_value)
    barcode128.barWidth = 1.1
    barcode128.drawOn(c, -10, 15)
    # 字符添加
    c.setFont('Times-Roman', 9)
    c.drawString(35, 3, barcode_value)
    # 二维码生成
    qr_code = qr.QrCodeWidget(barcode_value)
    bounds = qr_code.getBounds()
    width = bounds[2] - bounds[0]
    height = bounds[3] - bounds[1]
    d = Drawing(45, 45, transform=[45. / width, 0, 0, 45. / height, 0, 0])
    d.add(qr_code)
    renderPDF.draw(d, c, 60, 35)
    # 添加图片
    c.drawImage('.\img\img.jpg', 10, 40)


if __name__ == '__main__':
    while True:
        # 输入判断
        while True:
            v = input("please input 10 numbers:")
            regex_c = re.compile('^\\d{10}$')
            m = re.match(regex_c, v)
            if m:
                barcode_value = m.group(0)
                break
            else:
                print("wrong input")
                continue
        fname = 'p' + str(barcode_value) + '.pdf'
        c = canvas.Canvas(fname, pagesize=(114, 85))
        # 保存日志: 编号 时间
        # 获取时间
        t = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
        string = barcode_value + '\t\t' + t
        with open('log.txt', 'a+') as f:
            f.write(string + '\n')
        createBarCodes(c, barcode_value)
        c.showPage()
        c.save()

        GHOSTSCRIPT_PATH = "C:\\Program Files\\GHOSTSCRIPT\\bin\\gswin32.exe"
        GSPRINT_PATH = "C:\\Program Files\\GSPRINT\\gsprint.exe"
        loc = "D:\\python36\\python_program\\qrcodeGen"
        currentprinter = win32print.GetDefaultPrinter()
        x = 0
        for file in os.listdir(loc):
            if file.endswith('.pdf') and file != '':
                print("if")
                string = '-ghostscript "' + GHOSTSCRIPT_PATH + '" -printer "' + currentprinter + '" ' + file
                win32api.ShellExecute(0, 'open', GSPRINT_PATH, string, '.', 0)
                print('printing file >> ' + str(file))
                x = x + 1
                time.sleep(1)
        os.remove(fname)
