import random
import time
import traceback
from win10toast import ToastNotifier
import uiautomator2 as u2

toaster = ToastNotifier()

device = u2.connect()
bookingBtn = '//*[@resource-id="com.maytaste.ihealth:id/dept_list_view"]/android.widget.RelativeLayout[4]'
reservateId = 'com.maytaste.ihealth:id/btnReservation'
timeInfo = 'com.maytaste.ihealth:id/doctor_outpatient_time'

count = 0
while True:
    try:
        count += 1
        print('当前执行第' + str(count) + '次')
        device.xpath(bookingBtn).click()
        time.sleep(5)

        if device(resourceId=reservateId, enabled=True).exists:
            print('=================== 发现可预约目标 ==================')
            for item in device(resourceId=reservateId, enabled=True):
                timeText = item.left(resourceId=timeInfo).get_text()
                print('时间信息：' + timeText)
                if '2023-7-14' in timeText:
                    toaster.show_toast("有目标",
                                       device(resourceId='com.maytaste.ihealth:id/doctor_name').get_text(),
                                       duration=600)
            print('==================================================')
        else:
            print('没有课预约目标')
        device(text="返回").click()
        sleepTime = random.randint(15, 30)
        print('休眠：' + str(sleepTime) + "秒")
        time.sleep(sleepTime)
    except Exception as e:
        print(e.args)
        print("----------")
        print(traceback.format_exc())
        time.sleep(10)
        toaster.show_toast("告警", "执行失败", duration=10)

