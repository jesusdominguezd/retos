#!/usr/bin/python3
#Python3
#Author: Jesus Dominguez
#Script: check_ip.py
import sys
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import json

def check_ip_format(ip):
    ip_oct = ip.split('.')
    if len(ip_oct) < 4:
        print("Ingresa una IP valida")

def ibm_req(ip):
    url = "https://exchange.xforce.ibmcloud.com/ip/" + ip
    driver = webdriver.Firefox()
    driver.get(url)
    time.sleep(7)
    html = driver.page_source
    res = parse_html_ibm(html)
    driver.close()
    return res

def parse_html_ibm(web_page):
    res = {}
    content = BeautifulSoup(web_page, "html.parser")
    search_res = content.find(id="searchresults")
    # print(search_res)
    risk_level = search_res.find(class_="scorebackgroundfilter numtitle").string.extract().strip()
    res["Riesgo"] = risk_level
    categori = search_res.find(id="categories").find("td")
    try:
        res["Categorizacion"] = categori.string.extract().strip()
    except:
        res["Categorizacion"] = categori.find("span").string.extract().strip()
    country = search_res.find(id="country-of-ip").find("td")
    span = country.find("span")
    span.decompose()
    country = country.string.extract().strip()
    res["Ubicacion"] = country
    return res
    

def check_anon(ip, res):
    url = "https://spur.us/context/" + ip
    response = requests.get(url)
    if response.status_code != 200:
        print("El sitio https://spur.us/context/ no responde")
    else:
        res = parser_html_anon(response.content, res)
    return res

def parser_html_anon(web_page, res):
    content = BeautifulSoup(web_page, "html.parser")
    content = BeautifulSoup(web_page, "html.parser")
    search_res = content.find(id="preview")
    anon_serv = search_res.find(class_="ddc mb-3 text-left").find("span")
    if anon_serv == None:
        res["Anon service"] = "Not Anonymous"
    else:
        res["Anon service"] = anon_serv.string.extract().strip()
    return res

def check_ip(ip):
    resultado = ibm_req(ip)
    resultado = check_anon(ip, resultado)
    print("El resultado para la IP: " + ip + " es")
    print(json.dumps(resultado, indent = 4))

def print_help():
    print("Este script requiere python3\n")
    print("Usage: ./check_ip.py <IP>\neg: ./check_ip.py 8.8.8.8")

if __name__ == "__main__":
    print("IP Checker - Herramienta que revisa el status de un IP\n")
    if len(sys.argv) < 2 :
        print_help()
    else:
        ip = sys.argv[1]
        check_ip_format(ip)
        check_ip(ip)
        
