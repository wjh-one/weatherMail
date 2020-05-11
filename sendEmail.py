# @Time : 2020/4/21 13:08
# @Author : wjh

import smtplib
from email.mime.text import MIMEText


class SendEmail(object):
    def __init__(self, result, msg_to, city, msg_from, password):
        self.result = result
        self.msg_to = msg_to
        self.city = city
        self.msg_from = msg_from
        self.password = password

    def send(self):
        result = self.result
        day = result[0][0]
        tq0 = result[0][1]
        tq1 = result[0][2]
        tq2 = result[0][3]
        tq2 = int(tq2[0:-1])
        i = ''
        if tq1 is None:
            i = '未查询到'
        else:
            i = tq1
        todayWeather = '{}，最高温度{}℃，最低温度{}℃。<br>'.format(tq0, i, tq2)

        if tq1 is None:
            tq1 = -1
        else:
            tq1 = int(tq1)
        if tq1 == -1:
            todayWeather = todayWeather + "现在已经是下午了,早点回家"
            print(todayWeather)

        dressingIndex = '今天'
        if tq0.__contains__('雨'):
            dressingIndex = dressingIndex + "有雨，记得带伞！<br>"

        if tq0.__contains__('阴'):
            dressingIndex = dressingIndex + "阴天，可以不用带伞<br>"

        if tq0.__contains__('多云'):
            dressingIndex = dressingIndex + "多云，舒服的一天<br>"

        if tq0.__contains__('晴'):
            dressingIndex = dressingIndex + "晴天<br>"


        if tq2 <= 10:
            dressingIndex = dressingIndex + '早晚气温低于10℃！要注意保暖！<br>'
        else:
            dressingIndex = dressingIndex + '早晚气温高于10℃！穿薄点的衣物！<br>'


        if tq1 >= 20:
            dressingIndex = dressingIndex + '今天最高气温高于20℃！可以适当减少衣物！<br>'
        else:
            dressingIndex = dressingIndex + '今天最高气温低于20℃！减少衣物前请三思！<br>'

        print(dressingIndex)
        da = []

        for i in result:
            s = '{}，{}，最高温度{}，最低温度{}'.format(i[0], i[1], i[2], i[3])
            da.append(s)

        msg_from = self.msg_from  # 发送方邮箱
        passwd = self.password  # 填入发送方邮箱的授权码(填入自己的授权码，相当于邮箱密码)
        msg_to = self.msg_to  # 收件人邮箱

        subject = "一封温暖的天气预报"  # 主题

        message = '<br>'.join(da)
        print(message)

        content = '''
        <html>
         <head>
          <meta charset="utf-8" />
         </head>
         <body>
          <div class="content-wrap" style="margin: 0px auto; overflow: hidden; padding: 0px; border: 0px dotted rgb(238, 238, 238); width: 600px;">
           <!---->
           <div class="full" tindex="1" style="margin: 0px auto; max-width: 600px;">
            <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width: 600px;">
             <tbody>
              <tr>
               <td style="direction: ltr; width: 600px; font-size: 0px; padding-bottom: 0px; text-align: center; vertical-align: top; background-color: rgb(214, 214, 214); background-image: url(&quot;&quot;); background-repeat: no-repeat; background-size: 100px; background-position: 10% 50%;">
                <table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%" style="vertical-align: top;">
                 <tbody>
                  <tr>
                   <td align="left" style="font-size: 0px; padding: 50px 200px;">
                    <div class="text" style="font-family: 微软雅黑, &quot;Microsoft YaHei&quot;; overflow-wrap: break-word; margin: 0px; text-align: center; line-height: 20px; color: rgb(23, 32, 210); font-size: 20px; font-weight: normal;">
                     <div>
                      <p style="text-size-adjust: none; word-break: break-word; line-height: 20px; font-size: 30px; margin: 0px;">{}天气预报</p>
                     </div>
                    </div></td>
                  </tr>
                 </tbody>
                </table></td>
              </tr>
             </tbody>
            </table>
           </div>
           <div class="full" tindex="2" style="margin: 0px auto; line-height: 0px; max-width: 600px;">
            <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width: 600px;">
             <tbody>
              <tr>
               <td align="center" style="direction: ltr; font-size: 0px; padding: 20px; text-align: center; vertical-align: top; word-break: break-word; width: 600px; background-image: url(&quot;&quot;); background-repeat: no-repeat; background-size: 100px; background-position: 10% 50%;">
                <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse: collapse; border-spacing: 0px;">
                 <tbody>
                  <tr>
                   <td style="width: 375px; border-top: 1px solid rgb(204, 204, 204);"></td>
                  </tr>
                 </tbody>
                </table></td>
              </tr>
             </tbody>
            </table>
           </div>
           <div class="full" tindex="3" style="margin: 0px auto; max-width: 600px;">
            <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width: 600px;">
             <tbody>
              <tr>
               <td style="direction: ltr; width: 600px; font-size: 0px; padding-bottom: 0px; text-align: center; vertical-align: top; background-image: url(&quot;&quot;); background-repeat: no-repeat; background-size: 100px; background-position: 10% 50%;">
                <table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%" style="vertical-align: top;">
                 <tbody>
                  <tr>
                   <td align="left" style="font-size: 0px; padding: 5px 20px;">
                    <div class="text" style="font-family: 微软雅黑, &quot;Microsoft YaHei&quot;; overflow-wrap: break-word; margin: 0px; text-align: center; line-height: 20px; color: rgb(236, 11, 11); font-size: 18px; font-weight: normal;">
                     <div>
                      <p style="text-size-adjust: none; word-break: break-word; line-height: 20px; font-size: 30px; margin: 0px;">↓今日{}天气↓</p>
                     </div>
                    </div></td>
                  </tr>
                 </tbody>
                </table></td>
              </tr>
             </tbody>
            </table>
           </div>
           <div class="full" tindex="4" style="margin: 0px auto; line-height: 0px; max-width: 600px;">
            <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width: 600px;">
             <tbody>
              <tr>
               <td align="center" style="direction: ltr; font-size: 0px; padding: 20px; text-align: center; vertical-align: top; word-break: break-word; width: 600px; background-image: url(&quot;&quot;); background-repeat: no-repeat; background-size: 100px; background-position: 10% 50%;">
                <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse: collapse; border-spacing: 0px;">
                 <tbody>
                  <tr>
                   <td style="width: 375px; border-top: 1px solid rgb(204, 204, 204);"></td>
                  </tr>
                 </tbody>
                </table></td>
              </tr>
             </tbody>
            </table>
           </div>
           <div class="full" tindex="5" style="margin: 0px auto; max-width: 600px;">
            <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width: 600px;">
             <tbody>
              <tr>
               <td style="direction: ltr; width: 600px; font-size: 0px; padding-bottom: 0px; text-align: center; vertical-align: top; background-image: url(&quot;&quot;); background-repeat: no-repeat; background-size: 100px; background-position: 10% 50%;">
                <table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%" style="vertical-align: top;">
                 <tbody>
                  <tr>
                   <td align="left" style="font-size: 0px; padding: 35px 20px;">
                    <div class="text" style="font-family: 微软雅黑, &quot;Microsoft YaHei&quot;; overflow-wrap: break-word; margin: 0px; text-align: center; line-height: 25px; color: rgb(102, 102, 102); font-size: 14px; font-weight: normal;">
                     <div>
                      <p style="text-size-adjust: none; word-break: break-word; line-height: 30px; font-size: 25px; margin: 0px;">{}</p>
                     </div>
                    </div></td>
                  </tr>
                 </tbody>
                </table></td>
              </tr>
             </tbody>
            </table>
           </div>
           <div class="full" tindex="6" style="margin: 0px auto; line-height: 0px; max-width: 600px;">
            <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width: 600px;">
             <tbody>
              <tr>
               <td align="center" style="direction: ltr; font-size: 0px; padding: 20px; text-align: center; vertical-align: top; word-break: break-word; width: 600px; background-image: url(&quot;&quot;); background-repeat: no-repeat; background-size: 100px; background-position: 10% 50%;">
                <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse: collapse; border-spacing: 0px;">
                 <tbody>
                  <tr>
                   <td style="width: 375px; border-top: 1px solid rgb(204, 204, 204);"></td>
                  </tr>
                 </tbody>
                </table></td>
              </tr>
             </tbody>
            </table>
           </div>
           <div class="full" tindex="7" style="margin: 0px auto; max-width: 600px;">
            <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width: 600px;">
             <tbody>
              <tr>
               <td style="direction: ltr; width: 600px; font-size: 0px; padding-bottom: 0px; text-align: center; vertical-align: top; background-image: url(&quot;&quot;); background-repeat: no-repeat; background-size: 100px; background-position: 10% 50%;">
                <table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%" style="vertical-align: top;">
                 <tbody>
                  <tr>
                   <td align="left" style="font-size: 0px; padding: 5px 20px;">
                    <div class="text" style="font-family: 微软雅黑, &quot;Microsoft YaHei&quot;; overflow-wrap: break-word; margin: 0px; text-align: center; line-height: 20px; color: rgb(236, 11, 11); font-size: 18px; font-weight: normal;">
                     <div>
                      <p style="text-size-adjust: none; word-break: break-word; line-height: 20px; font-size: 30px; margin: 0px;">↓穿衣指南↓</p>
                     </div>
                    </div></td>
                  </tr>
                 </tbody>
                </table></td>
              </tr>
             </tbody>
            </table>
           </div>
           <div class="full" tindex="8" style="margin: 0px auto; line-height: 0px; max-width: 600px;">
            <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width: 600px;">
             <tbody>
              <tr>
               <td align="center" style="direction: ltr; font-size: 0px; padding: 20px; text-align: center; vertical-align: top; word-break: break-word; width: 600px; background-image: url(&quot;&quot;); background-repeat: no-repeat; background-size: 100px; background-position: 10% 50%;">
                <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse: collapse; border-spacing: 0px;">
                 <tbody>
                  <tr>
                   <td style="width: 375px; border-top: 1px solid rgb(204, 204, 204);"></td>
                  </tr>
                 </tbody>
                </table></td>
              </tr>
             </tbody>
            </table>
           </div>
           <div class="full" tindex="9" style="margin: 0px auto; max-width: 600px;">
            <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width: 600px;">
             <tbody>
              <tr>
               <td style="direction: ltr; width: 600px; font-size: 0px; padding-bottom: 0px; text-align: center; vertical-align: top; background-image: url(&quot;&quot;); background-repeat: no-repeat; background-size: 100px; background-position: 10% 50%;">
                <table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%" style="vertical-align: top;">
                 <tbody>
                  <tr>
                   <td align="left" style="font-size: 0px; padding: 35px 20px;">
                    <div class="text" style="font-family: 微软雅黑, &quot;Microsoft YaHei&quot;; overflow-wrap: break-word; margin: 0px; text-align: center; line-height: 25px; color: rgb(102, 102, 102); font-size: 14px; font-weight: normal;">
                     <div>
                      <p style="text-size-adjust: none; word-break: break-word; line-height: 30px; font-size: 25px; margin: 0px;">{}</p>
                     </div>
                    </div></td>
                  </tr>
                 </tbody>
                </table></td>
              </tr>
             </tbody>
            </table>
           </div>
           <div class="full" tindex="10" style="margin: 0px auto; line-height: 0px; max-width: 600px;">
            <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width: 600px;">
             <tbody>
              <tr>
               <td align="center" style="direction: ltr; font-size: 0px; padding: 20px; text-align: center; vertical-align: top; word-break: break-word; width: 600px; background-image: url(&quot;&quot;); background-repeat: no-repeat; background-size: 100px; background-position: 10% 50%;">
                <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse: collapse; border-spacing: 0px;">
                 <tbody>
                  <tr>
                   <td style="width: 375px; border-top: 1px solid rgb(204, 204, 204);"></td>
                  </tr>
                 </tbody>
                </table></td>
              </tr>
             </tbody>
            </table>
           </div>
           <div class="full" tindex="11" style="margin: 0px auto; max-width: 600px;">
            <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width: 600px;">
             <tbody>
              <tr>
               <td style="direction: ltr; width: 600px; font-size: 0px; padding-bottom: 0px; text-align: center; vertical-align: top; background-image: url(&quot;&quot;); background-repeat: no-repeat; background-size: 100px; background-position: 10% 50%;">
                <table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%" style="vertical-align: top;">
                 <tbody>
                  <tr>
                   <td align="left" style="font-size: 0px; padding: 5px 20px;">
                    <div class="text" style="font-family: 微软雅黑, &quot;Microsoft YaHei&quot;; overflow-wrap: break-word; margin: 0px; text-align: center; line-height: 20px; color: rgb(236, 11, 11); font-size: 18px; font-weight: normal;">
                     <div>
                      <p style="text-size-adjust: none; word-break: break-word; line-height: 20px; font-size: 28px; margin: 0px;">↓最近一周天气↓</p>
                     </div>
                    </div></td>
                  </tr>
                 </tbody>
                </table></td>
              </tr>
             </tbody>
            </table>
           </div>
           <div class="full" tindex="12" style="margin: 0px auto; line-height: 0px; max-width: 600px;">
            <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width: 600px;">
             <tbody>
              <tr>
               <td align="center" style="direction: ltr; font-size: 0px; padding: 20px; text-align: center; vertical-align: top; word-break: break-word; width: 600px; background-image: url(&quot;&quot;); background-repeat: no-repeat; background-size: 100px; background-position: 10% 50%;">
                <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse: collapse; border-spacing: 0px;">
                 <tbody>
                  <tr>
                   <td style="width: 375px; border-top: 1px solid rgb(204, 204, 204);"></td>
                  </tr>
                 </tbody>
                </table></td>
              </tr>
             </tbody>
            </table>
           </div>
           <div class="full" tindex="13" style="margin: 0px auto; max-width: 600px;">
            <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width: 600px;">
             <tbody>
              <tr>
               <td style="direction: ltr; width: 600px; font-size: 0px; padding-bottom: 0px; text-align: center; vertical-align: top; background-image: url(&quot;&quot;); background-repeat: no-repeat; background-size: 100px; background-position: 10% 50%;">
                <table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%" style="vertical-align: top;">
                 <tbody>
                  <tr>
                   <td align="left" style="font-size: 0px; padding: 35px 20px;">
                    <div class="text" style="font-family: 微软雅黑, &quot;Microsoft YaHei&quot;; overflow-wrap: break-word; margin: 0px; text-align: center; line-height: 25px; color: rgb(102, 102, 102); font-size: 14px; font-weight: normal;">
                     <div>
                      <p style="text-size-adjust: none; word-break: break-word; line-height: 30px; font-size: 25px; margin: 0px;">{}</p>
                     </div>
                    </div></td>
                  </tr>
                 </tbody>
                </table></td>
              </tr>
             </tbody>
            </table>
           </div>
          </div>
          <!---->
         </body>
        </html>
        '''.format(self.city, day, todayWeather, dressingIndex, message)

        # 生成一个MIMEText对象（还有一些其它参数）
        msg = MIMEText(content, 'html', 'utf-8')
        # 放入邮件主题
        msg['Subject'] = subject

        # 放入发件人
        msg['From'] = msg_from

        try:
            # 通过ssl方式发送，服务器地址，端口
            s = smtplib.SMTP_SSL("smtp.163.com")
            # 登录到邮箱
            s.login(msg_from, passwd)
            # 发送邮件：发送方，收件方，要发送的消息
            s.sendmail(msg_from, msg_to, msg.as_string())
            print('成功')
        except s.SMTPException as e:
            print(e)
        finally:
            s.quit()