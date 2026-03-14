import re
import httpx
from typing import Optional

PHONE_DATA = {
    "130": {"province": "广东", "city": "深圳", "isp": "中国联通", "area_code": "0755", "zip_code": "518000"},
    "131": {"province": "广东", "city": "广州", "isp": "中国联通", "area_code": "020", "zip_code": "510000"},
    "132": {"province": "北京", "city": "北京", "isp": "中国联通", "area_code": "010", "zip_code": "100000"},
    "133": {"province": "北京", "city": "北京", "isp": "中国电信", "area_code": "010", "zip_code": "100000"},
    "134": {"province": "广东", "city": "广州", "isp": "中国移动", "area_code": "020", "zip_code": "510000"},
    "135": {"province": "广东", "city": "广州", "isp": "中国移动", "area_code": "020", "zip_code": "510000"},
    "136": {"province": "广东", "city": "深圳", "isp": "中国移动", "area_code": "0755", "zip_code": "518000"},
    "137": {"province": "广东", "city": "广州", "isp": "中国移动", "area_code": "020", "zip_code": "510000"},
    "138": {"province": "上海", "city": "上海", "isp": "中国移动", "area_code": "021", "zip_code": "200000"},
    "139": {"province": "上海", "city": "上海", "isp": "中国移动", "area_code": "021", "zip_code": "200000"},
    "145": {"province": "北京", "city": "北京", "isp": "中国联通", "area_code": "010", "zip_code": "100000"},
    "147": {"province": "广东", "city": "广州", "isp": "中国移动", "area_code": "020", "zip_code": "510000"},
    "150": {"province": "北京", "city": "北京", "isp": "中国移动", "area_code": "010", "zip_code": "100000"},
    "151": {"province": "北京", "city": "北京", "isp": "中国移动", "area_code": "010", "zip_code": "100000"},
    "152": {"province": "上海", "city": "上海", "isp": "中国移动", "area_code": "021", "zip_code": "200000"},
    "153": {"province": "上海", "city": "上海", "isp": "中国电信", "area_code": "021", "zip_code": "200000"},
    "155": {"province": "北京", "city": "北京", "isp": "中国联通", "area_code": "010", "zip_code": "100000"},
    "156": {"province": "广东", "city": "广州", "isp": "中国联通", "area_code": "020", "zip_code": "510000"},
    "157": {"province": "浙江", "city": "杭州", "isp": "中国移动", "area_code": "0571", "zip_code": "310000"},
    "158": {"province": "浙江", "city": "杭州", "isp": "中国移动", "area_code": "0571", "zip_code": "310000"},
    "159": {"province": "浙江", "city": "杭州", "isp": "中国移动", "area_code": "0571", "zip_code": "310000"},
    "166": {"province": "北京", "city": "北京", "isp": "中国联通", "area_code": "010", "zip_code": "100000"},
    "170": {"province": "北京", "city": "北京", "isp": "中国电信", "area_code": "010", "zip_code": "100000"},
    "171": {"province": "北京", "city": "北京", "isp": "中国联通", "area_code": "010", "zip_code": "100000"},
    "172": {"province": "广东", "city": "广州", "isp": "中国移动", "area_code": "020", "zip_code": "510000"},
    "173": {"province": "北京", "city": "北京", "isp": "中国电信", "area_code": "010", "zip_code": "100000"},
    "175": {"province": "北京", "city": "北京", "isp": "中国联通", "area_code": "010", "zip_code": "100000"},
    "176": {"province": "广东", "city": "广州", "isp": "中国联通", "area_code": "020", "zip_code": "510000"},
    "177": {"province": "上海", "city": "上海", "isp": "中国电信", "area_code": "021", "zip_code": "200000"},
    "178": {"province": "浙江", "city": "杭州", "isp": "中国移动", "area_code": "0571", "zip_code": "310000"},
    "180": {"province": "上海", "city": "上海", "isp": "中国电信", "area_code": "021", "zip_code": "200000"},
    "181": {"province": "四川", "city": "成都", "isp": "中国电信", "area_code": "028", "zip_code": "610000"},
    "182": {"province": "四川", "city": "成都", "isp": "中国移动", "area_code": "028", "zip_code": "610000"},
    "183": {"province": "四川", "city": "成都", "isp": "中国移动", "area_code": "028", "zip_code": "610000"},
    "184": {"province": "四川", "city": "成都", "isp": "中国移动", "area_code": "028", "zip_code": "610000"},
    "185": {"province": "北京", "city": "北京", "isp": "中国联通", "area_code": "010", "zip_code": "100000"},
    "186": {"province": "上海", "city": "上海", "isp": "中国联通", "area_code": "021", "zip_code": "200000"},
    "187": {"province": "湖北", "city": "武汉", "isp": "中国移动", "area_code": "027", "zip_code": "430000"},
    "188": {"province": "湖北", "city": "武汉", "isp": "中国移动", "area_code": "027", "zip_code": "430000"},
    "189": {"province": "北京", "city": "北京", "isp": "中国电信", "area_code": "010", "zip_code": "100000"},
    "191": {"province": "北京", "city": "北京", "isp": "中国电信", "area_code": "010", "zip_code": "100000"},
    "193": {"province": "上海", "city": "上海", "isp": "中国电信", "area_code": "021", "zip_code": "200000"},
    "195": {"province": "北京", "city": "北京", "isp": "中国移动", "area_code": "010", "zip_code": "100000"},
    "196": {"province": "浙江", "city": "杭州", "isp": "中国联通", "area_code": "0571", "zip_code": "310000"},
    "197": {"province": "广东", "city": "广州", "isp": "中国移动", "area_code": "020", "zip_code": "510000"},
    "198": {"province": "北京", "city": "北京", "isp": "中国移动", "area_code": "010", "zip_code": "100000"},
    "199": {"province": "北京", "city": "北京", "isp": "中国电信", "area_code": "010", "zip_code": "100000"},
}


def is_valid_phone(phone: str) -> bool:
    if not phone:
        return False
    phone = re.sub(r'\s|-', '', phone)
    if re.match(r'^1[3-9]\d{9}$', phone):
        return True
    return False


def get_phone_prefix(phone: str) -> str:
    phone = re.sub(r'\s|-', '', phone)
    if len(phone) >= 7:
        return phone[:7]
    return phone[:3]


def get_phone_prefix_3(phone: str) -> str:
    phone = re.sub(r'\s|-', '', phone)
    return phone[:3]


async def lookup_phone(phone: str) -> Optional[dict]:
    if not is_valid_phone(phone):
        return None
    
    phone = re.sub(r'\s|-', '', phone)
    prefix_3 = get_phone_prefix_3(phone)
    prefix_7 = get_phone_prefix(phone)
    
    result = PHONE_DATA.get(prefix_3, {}).copy()
    
    if result:
        result["phone"] = phone
        result["phone_prefix"] = prefix_7
        return result
    
    result_online = await lookup_phone_online(phone)
    if result_online:
        return result_online
    
    return None


async def lookup_phone_online(phone: str) -> Optional[dict]:
    try:
        url = f"https://api.xtbts.com/api/phone/{phone}"
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.get(url)
            if response.status_code == 200:
                data = response.json()
                if data.get("success"):
                    return {
                        "phone": phone,
                        "phone_prefix": phone[:7],
                        "province": data.get("province", ""),
                        "city": data.get("city", ""),
                        "isp": data.get("isp", ""),
                        "area_code": data.get("area_code", ""),
                        "zip_code": data.get("zip_code", "")
                    }
    except:
        pass
    return None
