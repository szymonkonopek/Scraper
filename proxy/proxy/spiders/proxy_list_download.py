from typing import Iterable
import scrapy
from scrapy.http import Request
from ..items import ProxyItem

country_dict = {"Afghanistan": "AF", "Aland Islands": "AX", "Albania": "AL",
                "Algeria": "DZ", "American Samoa": "AS", "Andorra": "AD",
                "Angola": "AO", "Anguilla": "AI", "Antarctica": "AQ",
                "Antigua and Barbuda": "AG", "Argentina": "AR", "Armenia": "AM",
                "Aruba": "AW", "Australia": "AU", "Austria": "AT",
                "Azerbaijan": "AZ",
                "Bahamas": "BS", "Bahrain": "BH", "Bangladesh": "BD",
                "Barbados": "BB", "Belarus": "BY", "Belgium": "BE",
                "Belize": "BZ", "Benin": "BJ", "Bermuda": "BM", "Bhutan": "BT",
                "Bolivia": "BO", "Bosnia and Herzegovina": "BA",
                "Botswana": "BW", "Bouvet Island": "BV", "Brazil": "BR",
                "British Virgin Islands": "VG",
                "British Indian Ocean Territory": "IO",
                "Brunei Darussalam": "BN", "Bulgaria": "BG",
                "Burkina Faso": "BF", "Burundi": "BI",
                "Cambodia": "KH", "Cameroon": "CM", "Canada": "CA",
                "Cape Verde": "CV", "Cayman Islands": "KY",
                "Central African Republic": "CF", "Chad": "TD", "Chile": "CL",
                "China": "CN", "Hong Kong, SAR China": "HK",
                "Macao, SAR China": "MO", "Christmas Island": "CX",
                "Cocos (Keeling) Islands": "CC", "Colombia": "CO",
                "Comoros": "KM", "Congo (Brazzaville)": "CG",
                "Congo, (Kinshasa)": "CD", "Cook Islands": "CK",
                "Costa Rica": "CR", "Côte d'Ivoire": "CI", "Croatia": "HR",
                "Cuba": "CU", "Cyprus": "CY", "Czech Republic": "CZ",
                "Denmark": "DK", "Djibouti": "DJ", "Dominica": "DM",
                "Dominican Republic": "DO",
                "Ecuador": "EC", "Egypt": "EG", "El Salvador": "SV",
                "Equatorial Guinea": "GQ", "Eritrea": "ER", "Estonia": "EE",
                "Ethiopia": "ET",
                "Falkland Islands (Malvinas)": "FK", "Faroe Islands": "FO",
                "Fiji": "FJ", "Finland": "FI", "France": "FR",
                "French Guiana": "GF", "French Polynesia": "PF",
                "French Southern Territories": "TF",
                "Gabon": "GA", "Gambia": "GM", "Georgia": "GE", "Germany": "DE",
                "Ghana": "GH", "Gibraltar": "GI", "Greece": "GR",
                "Greenland": "GL", "Grenada": "GD", "Guadeloupe": "GP",
                "Guam": "GU", "Guatemala": "GT", "Guernsey": "GG",
                "Guinea": "GN", "Guinea-Bissau": "GW", "Guyana": "GY",
                "Haiti": "HT", "Heard and Mcdonald Islands": "HM",
                "Holy See (Vatican City State)": "VA", "Honduras": "HN",
                "Hungary": "HU",
                "Iceland": "IS", "India": "IN", "Indonesia": "ID",
                "Iran, Islamic Republic of": "IR", "Iraq": "IQ",
                "Ireland": "IE", "Isle of Man": "IM", "Israel": "IL",
                "Italy": "IT",
                "Jamaica": "JM", "Japan": "JP", "Jersey": "JE", "Jordan": "JO",
                "Kazakhstan": "KZ", "Kenya": "KE", "Kiribati": "KI",
                "Korea (North)": "KP", "Korea (South)": "KR", "Kuwait": "KW",
                "Kyrgyzstan": "KG",
                "Lao PDR": "LA", "Latvia": "LV", "Lebanon": "LB",
                "Lesotho": "LS", "Liberia": "LR", "Libya": "LY",
                "Liechtenstein": "LI", "Lithuania": "LT", "Luxembourg": "LU",
                "Macedonia, Republic of": "MK", "Madagascar": "MG",
                "Malawi": "MW", "Malaysia": "MY", "Maldives": "MV",
                "Mali": "ML", "Malta": "MT", "Marshall Islands": "MH",
                "Martinique": "MQ", "Mauritania": "MR", "Mauritius": "MU",
                "Mayotte": "YT", "Mexico": "MX",
                "Micronesia, Federated States of": "FM", "Moldova": "MD",
                "Monaco": "MC", "Mongolia": "MN", "Montenegro": "ME",
                "Montserrat": "MS", "Morocco": "MA", "Mozambique": "MZ",
                "Myanmar": "MM",
                "Namibia": "NA", "Nauru": "NR", "Nepal": "NP",
                "Netherlands": "NL", "Netherlands Antilles": "AN",
                "New Caledonia": "NC", "New Zealand": "NZ", "Nicaragua": "NI",
                "Niger": "NE", "Nigeria": "NG", "Niue": "NU",
                "Norfolk Island": "NF", "Northern Mariana Islands": "MP",
                "Norway": "NO",
                "Oman": "OM",
                "Pakistan": "PK", "Palau": "PW", "Palestinian Territory": "PS",
                "Panama": "PA", "Papua New Guinea": "PG", "Paraguay": "PY",
                "Peru": "PE", "Philippines": "PH", "Pitcairn": "PN",
                "Poland": "PL", "Portugal": "PT", "Puerto Rico": "PR",
                "Qatar": "QA",
                "Réunion": "RE", "Romania": "RO", "Russian Federation": "RU",
                "Rwanda": "RW",
                "Saint-Barthélemy": "BL", "Saint Helena": "SH",
                "Saint Kitts and Nevis": "KN", "Saint Lucia": "LC",
                "Saint-Martin (French part)": "MF",
                "Saint Pierre and Miquelon": "PM",
                "Saint Vincent and Grenadines": "VC", "Samoa": "WS",
                "San Marino": "SM", "Sao Tome and Principe": "ST",
                "Saudi Arabia": "SA", "Senegal": "SN", "Serbia": "RS",
                "Seychelles": "SC", "Sierra Leone": "SL", "Singapore": "SG",
                "Slovakia": "SK", "Slovenia": "SI", "Solomon Islands": "SB",
                "Somalia": "SO", "South Africa": "ZA",
                "South Georgia and the South Sandwich Islands": "GS",
                "South Sudan": "SS", "Spain": "ES", "Sri Lanka": "LK",
                "Sudan": "SD", "Suriname": "SR",
                "Svalbard and Jan Mayen Islands": "SJ", "Swaziland": "SZ",
                "Sweden": "SE", "Switzerland": "CH",
                "Syrian Arab Republic (Syria)": "SY",
                "Taiwan, Republic of China": "TW", "Tajikistan": "TJ",
                "Tanzania, United Republic of": "TZ", "Thailand": "TH",
                "Timor-Leste": "TL", "Togo": "TG", "Tokelau": "TK",
                "Tonga": "TO", "Trinidad and Tobago": "TT", "Tunisia": "TN",
                "Turkey": "TR", "Turkmenistan": "TM",
                "Turks and Caicos Islands": "TC", "Tuvalu": "TV",
                "Uganda": "UG", "Ukraine": "UA", "United Arab Emirates": "AE",
                "United Kingdom": "GB", "United States of America": "US",
                "US Minor Outlying Islands": "UM", "Uruguay": "UY",
                "Uzbekistan": "UZ",
                "Vanuatu": "VU", "Venezuela (Bolivarian Republic)": "VE",
                "Viet Nam": "VN", "Virgin Islands, US": "VI",
                "Wallis and Futuna Islands": "WF", "Western Sahara": "EH",
                "Yemen": "YE", "Zambia": "ZM", "Zimbabwe": "ZW"}


class ProxyListDownloadSpider(scrapy.Spider):
    name = "proxy-list.download"
    allowed_domains = ["www.proxy-lisy.download"]
    
    #start_urls = ["https://www.proxy-lisy.download"]

    def start_requests(self):
        #yield from
        code = 'US'
        name = "USA"
        yield scrapy.Request(
            f"https://www.proxy-list.download/api/v1/get?type=https&country={code}",
            callback=self.parse, meta={"country": {"name": name, "code": code}} )
            #for name, code in country_dict.items()

    def parse(self, response):
        for line in response.body.splitlines():
            proxy = line.decode()
            host, port = proxy.split(':')

            yield ProxyItem(**{"address": host, "port": port, "code": response.meta["country"]["code"],})



