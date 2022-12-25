#!/usr/bin/python3
import cgi
import pymysql.cursors
import os
import function
import sys
import datetime
from http import cookies

msg = []
check_radio_list = ["dnaflag", "humanflag", "drug_name", "reason"]
check_box_list = ["content18", "format1", "format2", "format3", "format4", "format5", "format6", "treatment6", "other_treatment", "other_place"]
check_dict = {}
error = {}
upload_dir = "../tmp"
cookie = function.get_user_name()
form = cgi.FieldStorage()

if cookie:
    user_name = cookie[0]["user_name"]
    #msg.append(f"<li>こんにちは{user_name}さん</li>")
    sql_Users = f"select user_id from Users where user_name = '{user_name}'"
    result_Users = function.connection_sql(sql_Users, "r", "mammals")
    user_id = result_Users[0]["user_id"]
    if form.list == []:
        function.open_html("../html/request.html", msg=msg, error=error)
    else:
        titlename = form.getfirst('titlename')
        dnaflag = form.getfirst('dnaflag')
        dna_approval_num = form.getfirst('dna_approval_num')
        humanflag = form.getfirst('humanflag')
        human_approval_num = form.getfirst('human_approval_num')
        drugflag = form.getfirst('drugflag')
        drug_name = form.getfirst('drug_name')
        resercher_name = form.getfirst('resercher_name')
        licence_num = form.getfirst('licence_num')
        purpose = form.getfirst('purpose')
        outline = form.getfirst('outline')
        start_time = form.getfirst('start_time')
        finish_time = form.getfirst('finish_time')
        reason = form.getfirst('reason')
        other_reason = form.getfirst('other_reason')
        categoly = form.getfirst('categoly')
        content1 = form.getfirst('content1')
        content2 = form.getfirst('content2')
        content3 = form.getfirst('content3')
        content4 = form.getfirst('content4')
        content5 = form.getfirst('content5')
        content6 = form.getfirst('content6')
        content7 = form.getfirst('content7')
        content8 = form.getfirst('content8')
        content9 = form.getfirst('content9')
        content10 = form.getfirst('content10')
        content11 = form.getfirst('content11')
        content12 = form.getfirst('content12')
        content13 = form.getfirst('content13')
        content14 = form.getfirst('content14')
        content15 = form.getfirst('content15')
        content16 = form.getfirst('content16')
        content17 = form.getfirst('content17')
        content18 = form.getfirst('content18')
        other_content = form.getfirst('other_content')
        format1 = form.getfirst('format1')
        format2 = form.getfirst('format2')
        format3 = form.getfirst('format3')
        format4 = form.getfirst('format4')
        format5 = form.getfirst('format5')
        format6 = form.getfirst('format6')
        format_drug_name = form.getfirst('format_drug_name')
        method_name = form.getfirst('method_name')
        content_num1 = form.getfirst('content_num1')
        content_num2 = form.getfirst('content_num2')
        content_num3 = form.getfirst('content_num3')
        content_num4 = form.getfirst('content_num4')
        content_num5 = form.getfirst('content_num5')
        content_num6 = form.getfirst('content_num6')
        treatment1 = form.getfirst('treatment1')
        treatment2 = form.getfirst('treatment2')
        treatment3 = form.getfirst('treatment3')
        treatment4 = form.getfirst('treatment4')
        treatment5 = form.getfirst('treatment5')
        treatment6 = form.getfirst('treatment6')
        other_treatment = form.getfirst('other_treatment')
        treatment_drug_name1 = form.getfirst('treatment_drug_name1')
        treatment_drug_name2 = form.getfirst('treatment_drug_name2')
        treatment_method_name1 = form.getfirst('treatment_method_name1')
        treatment_method_name2 = form.getfirst('treatment_method_name2')
        gas_name = form.getfirst('gas_name')
        animal = form.getfirst('animal')
        strain_name = form.getfirst('strain_name')
        male = form.getfirst('male')
        female = form.getfirst('female')
        age = form.getfirst('age')
        buy = form.getfirst('buy')
        out_distribution = form.getfirst("out_distribution")
        in_distribution = form.getfirst("in_distribution")
        breeding = form.getfirst("breeding")
        total = form.getfirst('total')
        quality = form.getfirst("quality")
        place = form.getfirst('place')
        other_place = form.getfirst('other_place')
        other_place_text = form.getfirst('other_place_text')
        remarks = form.getfirst('remarks')
        zip_file = ""
        file_name = ""
        zip_file= form.getfirst('zip_file')
        documents = ""
        confirm_2 = ""
        confirm_3 = ""
        confirm_4 = ""
        confirm_8 = ""
        confirm_10 = ""
        confirm_11 = ""
        confirm_12 = ""
        confirm_13 = ""
        
        if zip_file != None or zip_file != "":
            if 'zip_file' in form.list:
                file_item = form['zip_file']
                if file_item.filename:
                    file_name = file_item.filename
                    with open(os.path.join("../tmp", file_name), "wb") as f:
                        f.write(file_item.file.read())
                        zip_file = f"../tmp/{file_name}"                        
        else:
            zip_file = "なし"
            file_name = "なし"
            
        check_box_dict = {"content18":other_content, "format1":content_num1, "format2":content_num2, "format3":content_num3, "format4":content_num4, "format5":content_num5, "format6":content_num6,  "treatment3":gas_name, "treatment6":other_treatment,  "other_place":other_place_text}
        
        check_radio_dict = {"dnaflag":dna_approval_num, "humanflag":human_approval_num, "drug_name":drug_name, "reason":other_reason}
        for check in check_box_list:
            if form.getfirst(check) != None and (check_box_dict[check] == None or check_box_dict[check] == ''):
                error["error"] = f"チェックが入っている状態で必要なテキストが入力されていない箇所があります{form.getfirst(check)}"
                function.open_html("../html/request.html", error=error)
                break
        for check in check_radio_list:
            if form.getfirst(check) == "1" and (check_radio_dict[check] == None or check_dict[check] == ""):
                error["error"] = "使用すると選択しているが必要なテキストが入力されていない箇所があります"
                function.open_html("../html/request.html", error=error)
                break
            
        if dnaflag=="1":
            confirm_2 = dna_approval_num
        else:
            confirm_2 = "使用しない"
        if humanflag=="1":
            confirm_3 = human_approval_num
        else:
            confirm_3 = "使用しない"
        if drugflag=="1":
            confirm_4 = f"{drug_name}\n{resercher_name}\n{licence_num}"
        else:
            confirm_4 = "使用しない"
        if reason=="その他":
            confirm_8 = other_reason
        else:
            confirm_8 = reason
        
        content_list = [content1, content2, content3, content4, content5, content6, content7, content8, content9, content10, content11, content12, content13, content14, content15, content16, content17, content18]
        for content in content_list:
            if content=="その他":
                confirm_10 = f"{other_content}, "
            elif content != None:
                confirm_10 += f"{content}, " 
        
        format_list = [format1, format2, format3, format4, format5, format6]
        format_dict = {format1:content_num1, format2:content_num2, format3:content_num3, format4:content_num4, format5:content_num5, format6:content_num6}
        for format in format_list:
            if format=="苦痛の排除のため、麻酔薬・鎮痛薬を使用する実験である" and format != None:
                confirm_11 += f"{format3}({content_num3} 薬品名：{format_drug_name} 投与方法：{method_name})\n"
            elif format != None:
                content_num = format_dict[format]
                confirm_11 += f"{format}({content_num})\n"
        
        treatment_list = [treatment1, treatment2, treatment3, treatment4, treatment5, treatment6]
        for treatment in treatment_list:
            if treatment=="過麻酔":
                confirm_12 += f"{treatment1} 薬品名：{treatment_drug_name1} 投与方法：{treatment_method_name1}\n"
            elif treatment=="過麻酔+放血":
                confirm_12 += f"{treatment1} 薬品名：{treatment_drug_name1} 投与方法：{treatment_method_name1}\n"
            elif treatment=="ガス吸入" :
                confirm_12 += f"{treatment} 吸入法・ガス名{gas_name}\n"
            elif treatment=="その他":
                confirm_12 += f"{other_treatment}\n"
            elif treatment != None:
                 confirm_12 += f"{treatment}\n"
        
        place_list = [animal, strain_name, male, female, age, buy, out_distribution, in_distribution, breeding, total, quality, place, other_place]
        for place in place_list:
            if place != None:
                confirm_13 += f"{place}, "
        
       # today = datetime.date.today()
       # form_start_date = datetime.datetime.fromisoformat(start_time)
       # form_finish_date = datetime.datetime.fromisoformat("2022-01-01")
       # if (today > form_start_date) or (today > form_finish_date):
       #     error["error"] = "開始日時あるいは終了日時が現在日時より古い日時になっています"
        #    function.open_html("../html/request.html", error=error)
        
        msg.extend([titlename, dnaflag, dna_approval_num, humanflag, human_approval_num, drugflag, drug_name, resercher_name, licence_num, purpose, outline, start_time, finish_time, reason, other_reason, categoly, format1, content_num1, format2, content_num2, format3, content_num3, format_drug_name, method_name, format4, content_num4, format5, content_num5, format6, content_num6, treatment1, treatment_drug_name1, treatment_method_name1, treatment2, treatment_drug_name2, treatment_method_name2, treatment3, gas_name, treatment4, treatment5, treatment6, other_treatment, remarks, content1, content2, content3, content4, content5, content6, content7, content8, content9, content10, content11, content12, content13, content14, content15, content16, content17, content18, other_content, zip_file, file_name, animal, strain_name, male, female, age, buy, out_distribution, in_distribution, breeding, total, place, other_place, other_place_text, quality, confirm_2, confirm_3, confirm_4, confirm_8, confirm_10, confirm_11, confirm_12, confirm_13])
        function.open_html("../html/confirm.html",msg=msg)
           
else:
    print("Location:./login.cgi\n")