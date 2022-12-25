#!/usr/bin/python3
import pymysql.cursors
import cgi 
import os
import function
import datetime

msg = []
error = {}
form = cgi.FieldStorage()
cookie = function.get_user_name()

if cookie:
    user_name = cookie[0]["user_name"]
    sql_Users = f"select user_id from Users where user_name = '{user_name}'"
    result_Users = function.connection_sql(sql_Users, "r", "mammals")
    user_id = result_Users[0]["user_id"]
    
    if form.list == []:
        function.open_html("../../html/mammals/request.html")
    else:
        titlename = form.getfirst('titlename')
        dnaflag = form.getfirst('dnaflag')
        dna_approval_num = form.getfirst('dna_approval_num', "")
        humanflag = form.getfirst('humanflag')
        human_approval_num = form.getfirst('human_approval_num', "")
        drugflag = form.getfirst('drugflag')
        drug_name = form.getfirst('drug_name', "")
        resercher_name = form.getfirst('resercher_name', "")
        licence_num = form.getfirst('lisence_num', "")
        purpose = form.getfirst('purpose')
        outline = form.getfirst('outline')
        start_time = form.getfirst('start_time')
        finish_time = form.getfirst('finish_time')
        reason = form.getfirst('reason')
        other_reason = form.getfirst('other_reason', "")
        categoly = form.getfirst('categoly')
        content1 = form.getfirst('content1', "")
        content2 = form.getfirst('content2', "")
        content3 = form.getfirst('content3', "")
        content4 = form.getfirst('content4', "")
        content5 = form.getfirst('content5', "")
        content6 = form.getfirst('content6', "")
        content7 = form.getfirst('content7', "")
        content8 = form.getfirst('content8', "")
        content9 = form.getfirst('content9', "")
        content10 = form.getfirst('content10', "")
        content11 = form.getfirst('content11', "")
        content12 = form.getfirst('content12', "")
        content13 = form.getfirst('content13', "")
        content14 = form.getfirst('content14', "")
        content15 = form.getfirst('content15', "")
        content16 = form.getfirst('content16', "")
        content17 = form.getfirst('content17', "")
        content18 = form.getfirst('content18', "")
        other_content = form.getfirst('other_content', "")
        format1 = form.getfirst('format1', "")
        format2 = form.getfirst('format2', "")
        format3 = form.getfirst('format3', "")
        format4 = form.getfirst('format4', "")
        format5 = form.getfirst('format5', "")
        format6 = form.getfirst('format6', "")
        format_drug_name = form.getfirst('format_drug_name', "")
        method_name = form.getfirst('method_name', "")
        content_num1 = form.getfirst('content_num1', "")
        content_num2 = form.getfirst('content_num2', "")
        content_num3 = form.getfirst('content_num3', "")
        content_num4 = form.getfirst('content_num4', "")
        content_num5 = form.getfirst('content_num5', "")
        content_num6 = form.getfirst('content_num6', "")
        treatment1 = form.getfirst('treatment1', "")
        treatment2 = form.getfirst('treatment2', "")
        treatment3 = form.getfirst('treatment3', "")
        treatment4 = form.getfirst('treatment4', "")
        treatment5 = form.getfirst('treatment5', "")
        treatment6 = form.getfirst('treatment6', "")
        other_treatment = form.getfirst('other_treatment', "")
        treatment_drug_name1 = form.getfirst('treatment_drug_name1', "")
        treatment_drug_name2 = form.getfirst('treatment_drug_name2', "")
        treatment_method_name1 = form.getfirst('treatment_method_name1', "")
        treatment_method_name2 = form.getfirst('treatment_method_name2', "")
        gas_name = form.getfirst('gas_name', "")
        remarks = form.getfirst('remarks', "")
        zip_file = form.getfirst("zip_file", "")
        animal = form.getfirst("animal")
        strain_name = form.getfirst("strain_name")
        male = form.getfirst("male", "")
        female = form.getfirst("female", "")
        age = form.getfirst("age", "")
        buy = form.getfirst("buy", "")
        out_distribution = form.getfirst("out_distribution", "")
        in_distribution = form.getfirst("in_distribution", "")
        breeding = form.getfirst("breeding", "")
        total = form.getfirst("total", "")
        quality = form.getfirst("quality")
        place = form.getfirst("place", "")
        other_place = form.getfirst("other_place", "")
        other_place_text = form.getfirst("other_place_text", "")
        now_date = datetime.datetime.now()
        request_date = now_date.strftime("%Y/%m/%d")

        sql_request = f"INSERT INTO request (request_id, user_id, experiment_num, titlename, dnaflag, dna_appproval_num, humanflag, human_approval_num, drugflag, drug_name, resercher_name, licence_num, purpose, outline, start_time, finish_time, reason, other_reason, category, format1, content_num1, format2, content_num2, format3, content_num3, format_drug_name, method_name, format4, content_num4, format5, content_num5, format6, content_num6, treatment1, treatment_drug_name1, treatment_method_name1, treatment2, treatment_drug_name2, treatment_method_name2, treatment3, gas_name, treatment4, treatment5, treatment6, other_treatment, remarks, zip_file, allow, request_date) values (null, {user_id}, '', '{titlename}', '{dnaflag}',  '{dna_approval_num}', '{humanflag}', '{human_approval_num}', '{drugflag}', '{drug_name}',  '{resercher_name}', '{licence_num}', '{purpose}', '{outline}',  '{start_time}', '{finish_time}', '{reason}', '{other_reason}', '{categoly}', '{format1}', '{content_num1}', '{format2}', '{content_num2}', '{format3}', '{content_num3}', '{format_drug_name}', '{method_name}', '{format4}', '{content_num4}', '{format5}', '{content_num5}', '{format6}', '{content_num6}', '{treatment1}', '{treatment_drug_name1}', '{treatment_method_name1}', '{treatment2}', '{treatment_drug_name2}', '{treatment_method_name2}', '{treatment3}', '{gas_name}', '{treatment4}', '{treatment5}', '{treatment6}', '{other_treatment}', '{remarks}', '{zip_file}', '0', '{request_date}')" 
        function.connection_sql(sql_request, "w", "mammals")

        get_request_id = f"select request_id from request where titlename = '{titlename}' and request_date = '{request_date}'"
        result_request = function.connection_sql(get_request_id, "r", "mammals")
        request_id = result_request[0]["request_id"]

        sql_experiment_content = "INSERT INTO Experiment_content (request_id, content1, content2, content3, content4, content5, content6, content7, content8, content9, content10, content11, content12, content13, content14, content15, content16, content17, content18, other_content)" 
        sql_experiment_content += f"VALUES ({request_id}, '{content1}', '{content2}', '{content3}', '{content4}', '{content5}', '{content6}', '{content7}', '{content8}', '{content9}', '{content10}', '{content11}', '{content12}', '{content13}', '{content14}', '{content15}', '{content16}', '{content17}', '{content18}', '{other_content}')"
        function.connection_sql(sql_experiment_content, "w", "mammals")
        
        sql_Place = "insert into Place (place_id, request_id, animal, strain_name, male, female, age, buy, out_distribution, in_distribution, breeding, total, quality, place, other_place, other_place_text)"
        sql_Place += f"values (null, {request_id}, '{animal}', '{strain_name}', '{male}', '{female}', '{age}', '{buy}', '{out_distribution}', '{in_distribution}', '{breeding}', '{total}', '{quality}', '{place}', '{other_place}', '{other_place_text}')"
        function.connection_sql(sql_Place, "w", "mammals") 

        msg.append(request_id)
        function.open_html("../../html/mammals/out.html", msg=msg)
else:
    print("Locaion:./login.cgi")