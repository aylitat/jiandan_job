
import tomxin.getInfo

def getTYUT():
#太原理工大学
# if __name__ == '__main__':
    url = "http://jiuye.tyut.edu.cn/zpweb/qyzp_sy.aspx"#高校就业网的网址
    html = tomxin.getInfo.get_source(url,"utf-8")
    info = tomxin.getInfo.get_info(html,'更新日期','</table>')
    title = tomxin.getInfo.get_content(info,'CompanyDetail.+?title=','target')
    url = tomxin.getInfo.get_content(info,'CompanyDetail','"')
    i=0
    for u in url[:]:
        r_city="山西"
        r_school="太原理工大学"
        r_title=title[i]
        r_trait = "TYUT" + u[-5:]#这里要自己写提取规则
        r_url = "http://jiuye.tyut.edu.cn/zpweb/Job/Job_CompanyDetail" + u
        i += 1
        r_content = tomxin.getInfo.get_url_content(r_url, "utf-8", '企业简介.+?</tr>', '<td height="35"')
        print(r_title + "\n" + r_url)

