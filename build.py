#!/usr/bin/env python3
"""Static site generator for Elevantec Company / شركة إليفانتك (Arabic + English).

Run `python3 build.py` after editing the content below. It rewrites every
HTML page, sitemap.xml, robots.txt and 404.html. No dependencies beyond Python 3.
"""
import json, os, hashlib

def _v(p): return hashlib.md5(open(p, "rb").read()).hexdigest()[:8]
ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)
CSS = "/assets/css/style.css?v=" + _v("assets/css/style.css")
JS = "/assets/js/main.js?v=" + _v("assets/js/main.js")

# ---------------------------------------------------------------- settings (EDIT THESE)
SITE = "https://elevantec.sa"            # reserved domain
EMAIL = "info@elevantec.sa"
PRIVACY_EMAIL = "privacy@elevantec.sa"
PHONE_DISPLAY = "+966 50 020 9038"                   # e.g. "+966 5X XXX XXXX"; empty hides the phone rows
PHONE_TEL = "+966500209038"                       # e.g. "+9665XXXXXXXX"
LINKEDIN_URL = "https://www.linkedin.com/company/elevantec/"                    # empty hides the LinkedIn icon (footer) and row (contact); set when the page exists
SUPPORT_EMAIL = "support@elevantec.sa"
BOOKING_URL = ""                     # Cal.com / Calendly link; empty hides the "book a call" button
CR = "7050745707"                    # same legal entity as Maya AI / Sahm Alkarar
# Contact form: empty endpoint = opens the visitor's email app. For Web3Forms use
# FORM_ENDPOINT = "https://api.web3forms.com/submit" and put the access key in FORM_KEY.
FORM_ENDPOINT = "https://api.web3forms.com/submit"   # Web3Forms; "" = mailto fallback
FORM_KEY = "843ee7ab-d506-48fc-a351-fb3d3ba869f9"   # public access key, delivers to info@elevantec.sa

_P = lambda f: f'<link rel="preload" href="/assets/fonts/{f}-normal.woff2" as="font" type="font/woff2" crossorigin>\n'
PRELOAD = {"ar": _P("ibm-plex-sans-arabic-arabic-400") + _P("noto-kufi-arabic-arabic-700"),
           "en": _P("ibm-plex-sans-latin-400") + _P("ibm-plex-sans-latin-600")}

import re as _re
def CICON(n, cls="cicon"):
    svg = open(f"/home/claude/brand/carbon/icons/{n}.svg").read().strip()
    return _re.sub(r'<svg[^>]*>', f'<svg class="{cls}" fill="currentColor" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" aria-hidden="true" focusable="false">', svg, count=1).replace("\n", " ").replace("\t", " ")
ICONS = {  # IBM Carbon pictograms (Apache 2.0)
 "ai": '<svg class="icon" fill="currentColor" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" aria-hidden="true" focusable="false"><path d="M12,1.64c-0.002,0-0.004,0-0.006,0c-1.473,0-2.691,0.759-3.239,2h-0.48 c-0.003,0-0.006,0-0.009,0c-1.271,0-2.478,0.425-3.398,1.199C3.892,5.659,3.354,6.79,3.352,8.021 c-0.001,0.995,0.526,2.097,1.025,2.791c-2.223,0.77-3.734,2.633-3.737,4.688c-0.003,2.046,1.507,3.91,3.734,4.687 c-0.506,0.692-1.044,1.788-1.045,2.766c-0.003,2.426,2.215,4.403,4.947,4.408h0.48c0.543,1.238,1.764,1.998,3.244,2 c0.002,0,0.004,0,0.007,0c1.972,0,3.351-1.381,3.354-3.36V5C15.363,3.025,13.982,1.643,12,1.64z M12,18.64 c-0.353,0-0.64-0.287-0.64-0.64s0.287-0.64,0.64-0.64s0.64,0.287,0.64,0.64S12.353,18.64,12,18.64z M14.64,13.64h-2.28V7.305 c0.575-0.159,1-0.681,1-1.305c0-0.75-0.61-1.36-1.36-1.36S10.64,5.25,10.64,6c0,0.625,0.425,1.146,1,1.305v6.335H10 c-0.001,0-0.001,0-0.002,0C9.2,13.64,8.641,14.199,8.64,15v0.64H6.305c-0.159-0.575-0.681-1-1.305-1c-0.75,0-1.36,0.61-1.36,1.36 S4.25,17.36,5,17.36c0.625,0,1.147-0.426,1.305-1H8.64v5.834c-0.575,0.159-1,0.681-1,1.306c0,0.75,0.61,1.36,1.36,1.36 s1.36-0.61,1.36-1.36c0-0.625-0.425-1.147-1-1.306V15c0.001-0.401,0.239-0.641,0.639-0.641H10h4.64v11.639 c-0.003,1.456-0.908,2.46-2.28,2.61v-9.303c0.575-0.159,1-0.681,1-1.306c0-0.75-0.61-1.36-1.36-1.36s-1.36,0.61-1.36,1.36 c0,0.625,0.425,1.147,1,1.306v9.31c-1.103-0.114-1.951-0.742-2.3-1.735C9.289,26.736,9.153,26.64,9,26.64H8.276 c-2.036-0.003-4.23-1.413-4.228-3.686c0.002-0.966,0.714-2.209,1.206-2.699c0.092-0.091,0.127-0.225,0.093-0.35 s-0.132-0.222-0.257-0.254c-2.199-0.566-3.733-2.273-3.73-4.151c0.003-1.876,1.522-3.573,3.695-4.141h2.64 c0.159,0.575,0.681,1,1.305,1c0.75,0,1.36-0.61,1.36-1.36S9.75,9.64,9,9.64c-0.625,0-1.146,0.425-1.305,1H5.162 C4.685,10.099,4.07,8.949,4.071,8.022C4.073,7.006,4.52,6.072,5.332,5.39c0.779-0.655,1.849-1.03,2.936-1.03 c0.002,0,0.005,0,0.008,0H9c0.152,0,0.288-0.096,0.339-0.239c0.392-1.103,1.384-1.761,2.655-1.761c0.002,0,0.003,0,0.005,0 C13.582,2.363,14.643,3.423,14.64,5V13.64z M12,6.64c-0.353,0-0.64-0.287-0.64-0.64S11.647,5.36,12,5.36S12.64,5.647,12.64,6 S12.353,6.64,12,6.64z M9,22.86c0.353,0,0.64,0.287,0.64,0.64S9.353,24.14,9,24.14s-0.64-0.287-0.64-0.64S8.647,22.86,9,22.86z M5.64,16c0,0.353-0.287,0.64-0.64,0.64S4.36,16.353,4.36,16S4.647,15.36,5,15.36S5.64,15.647,5.64,16z M8.36,11 c0-0.353,0.287-0.64,0.64-0.64S9.64,10.647,9.64,11S9.353,11.64,9,11.64S8.36,11.353,8.36,11z M31.36,15.5 c0.002-2.046-1.508-3.909-3.734-4.687c0.507-0.692,1.044-1.788,1.046-2.767c0.002-1.231-0.54-2.365-1.526-3.193 c-0.917-0.77-2.163-1.212-3.421-1.214h-0.48c-0.544-1.238-1.764-1.998-3.243-2c-0.003,0-0.005,0-0.008,0 c-0.972,0-1.808,0.323-2.418,0.933C16.965,3.185,16.642,4.023,16.64,5v20.999c-0.003,1.976,1.378,3.357,3.359,3.361 c0.003,0,0.005,0,0.007,0c1.473,0,2.69-0.76,3.238-2h0.479c0.004,0,0.007,0,0.01,0c1.271,0,2.478-0.426,3.398-1.199 c0.977-0.82,1.515-1.95,1.517-3.182c0.001-0.995-0.526-2.098-1.025-2.791C29.847,19.418,31.357,17.555,31.36,15.5z M20,12.36 c0.353,0,0.64,0.287,0.64,0.64s-0.287,0.64-0.64,0.64s-0.64-0.287-0.64-0.64S19.647,12.36,20,12.36z M26.946,19.64h-2.641 c-0.159-0.575-0.681-1-1.306-1c-0.75,0-1.36,0.61-1.36,1.36s0.61,1.36,1.36,1.36c0.624,0,1.147-0.425,1.306-1h2.533 c0.476,0.541,1.091,1.691,1.089,2.618c-0.001,1.016-0.448,1.95-1.26,2.631c-0.781,0.657-1.865,1.01-2.943,1.03H23 c-0.152,0-0.288,0.097-0.339,0.239c-0.393,1.104-1.385,1.761-2.655,1.761c-0.002,0-0.004,0-0.005,0 c-0.781-0.001-1.445-0.252-1.919-0.725C17.608,27.441,17.358,26.78,17.36,26v-8.64h2.279v6.334c-0.575,0.159-1,0.681-1,1.306 c0,0.75,0.61,1.36,1.36,1.36s1.36-0.61,1.36-1.36c0-0.624-0.425-1.147-1-1.306V17.36h1.639c0.001,0,0.002,0,0.003,0 c0.799,0,1.356-0.559,1.358-1.36v-0.64h2.334c0.159,0.575,0.681,1,1.306,1c0.75,0,1.36-0.61,1.36-1.36s-0.61-1.36-1.36-1.36 c-0.625,0-1.147,0.425-1.306,1H23.36V8.805c0.575-0.159,1-0.681,1-1.305c0-0.75-0.61-1.36-1.36-1.36s-1.36,0.61-1.36,1.36 c0,0.624,0.425,1.146,1,1.305V16c0,0.401-0.238,0.641-0.638,0.641c-0.001,0-0.001,0-0.002,0h-4.64V5 c0.001-0.781,0.252-1.445,0.725-1.918c0.397-0.398,0.933-0.627,1.555-0.693v9.305c-0.575,0.159-1,0.681-1,1.305 c0,0.75,0.61,1.36,1.36,1.36s1.36-0.61,1.36-1.36c0-0.624-0.425-1.146-1-1.305v-9.31c1.103,0.115,1.951,0.742,2.3,1.736 c0.051,0.144,0.188,0.24,0.34,0.24h0.724c1.092,0.001,2.17,0.383,2.959,1.045c0.82,0.689,1.271,1.626,1.269,2.641 c-0.001,0.966-0.714,2.209-1.205,2.699c-0.092,0.091-0.127,0.225-0.094,0.35c0.034,0.125,0.133,0.222,0.258,0.254 c2.198,0.567,3.732,2.274,3.729,4.151C30.638,17.374,29.12,19.07,26.946,19.64z M23.64,20c0,0.353-0.287,0.64-0.64,0.64 s-0.64-0.287-0.64-0.64s0.287-0.64,0.64-0.64S23.64,19.647,23.64,20z M20,24.36c0.353,0,0.64,0.287,0.64,0.64s-0.287,0.64-0.64,0.64 s-0.64-0.287-0.64-0.64S19.647,24.36,20,24.36z M23,8.14c-0.353,0-0.64-0.287-0.64-0.64S22.647,6.86,23,6.86s0.64,0.287,0.64,0.64 S23.353,8.14,23,8.14z M26.36,15c0-0.353,0.287-0.64,0.64-0.64s0.64,0.287,0.64,0.64s-0.287,0.64-0.64,0.64S26.36,15.353,26.36,15z"/></svg>',
 "geo": '<svg class="icon" fill="currentColor" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" aria-hidden="true" focusable="false"><path d="M15,31.36h-3c-0.199,0-0.36-0.161-0.36-0.36v-3c0-0.199,0.161-0.36,0.36-0.36h3 c0.199,0,0.36,0.161,0.36,0.36v3C15.36,31.199,15.199,31.36,15,31.36z M12.36,30.64h2.28v-2.28h-2.28V30.64z M30,30.36h-4 c-0.199,0-0.36-0.161-0.36-0.36v-4c0-0.199,0.161-0.36,0.36-0.36h4c0.199,0,0.36,0.161,0.36,0.36v4 C30.36,30.199,30.199,30.36,30,30.36z M26.36,29.64h3.279v-3.28H26.36V29.64z M10,26.36H4c-0.199,0-0.36-0.161-0.36-0.36v-5.64H2 c-0.199,0-0.36-0.161-0.36-0.36v-2c0-0.199,0.161-0.36,0.36-0.36h2c0.199,0,0.36,0.161,0.36,0.36v1.64H10 c0.199,0,0.36,0.161,0.36,0.36v6C10.36,26.199,10.199,26.36,10,26.36z M4.36,25.64h5.28v-5.28H4.36V25.64z M2.36,19.64h1.28v-1.28 H2.36V19.64z M24,25.36h-4c-0.199,0-0.36-0.161-0.36-0.36v-4c0-0.199,0.161-0.36,0.36-0.36h4c0.199,0,0.36,0.161,0.36,0.36v4 C24.36,25.199,24.199,25.36,24,25.36z M20.36,24.64h3.279v-3.28H20.36V24.64z M31,21.36h-3c-0.199,0-0.36-0.161-0.36-0.36v-3 c0-0.199,0.161-0.36,0.36-0.36h3c0.199,0,0.36,0.161,0.36,0.36v3C31.36,21.199,31.199,21.36,31,21.36z M28.36,20.64h2.279v-2.28 H28.36V20.64z M16,21.36h-2c-0.199,0-0.36-0.161-0.36-0.36v-2c0-0.199,0.161-0.36,0.36-0.36h1.64V16c0-0.199,0.161-0.36,0.36-0.36h3 c0.199,0,0.36,0.161,0.36,0.36v3c0,0.199-0.161,0.36-0.36,0.36h-2.64V21C16.36,21.199,16.199,21.36,16,21.36z M14.36,20.64h1.28 v-1.28h-1.28V20.64z M16.36,18.64h2.28v-2.28h-2.28V18.64z M26,16.36h-2c-0.199,0-0.36-0.161-0.36-0.36v-2 c0-0.199,0.161-0.36,0.36-0.36h2c0.199,0,0.36,0.161,0.36,0.36v2C26.36,16.199,26.199,16.36,26,16.36z M24.36,15.64h1.279v-1.28 H24.36V15.64z M7,16.36H4c-0.199,0-0.36-0.161-0.36-0.36v-2.64H1c-0.199,0-0.36-0.161-0.36-0.36v-3c0-0.199,0.161-0.36,0.36-0.36 h2.64V8c0-0.199,0.161-0.36,0.36-0.36h2c0.199,0,0.36,0.161,0.36,0.36v2c0,0.199-0.161,0.36-0.36,0.36H4.36v2.28H7 c0.199,0,0.36,0.161,0.36,0.36v3C7.36,16.199,7.199,16.36,7,16.36z M4.36,15.64h2.28v-2.28H4.36V15.64z M1.36,12.64h2.28v-2.28H1.36 V12.64z M4.36,9.64h1.28V8.36H4.36V9.64z M14,14.36h-2c-0.199,0-0.36-0.161-0.36-0.36v-2c0-0.199,0.161-0.36,0.36-0.36h1.64V6 c0-0.199,0.161-0.36,0.36-0.36h6c0.199,0,0.36,0.161,0.36,0.36v6c0,0.199-0.161,0.36-0.36,0.36h-5.64V14 C14.36,14.199,14.199,14.36,14,14.36z M12.36,13.64h1.28v-1.28h-1.28V13.64z M14.36,11.64h5.28V6.36h-5.28 C14.36,6.36,14.36,11.64,14.36,11.64z M28,10.36h-3c-0.199,0-0.36-0.161-0.36-0.36V7c0-0.199,0.161-0.36,0.36-0.36h2.64V5 c0-0.199,0.161-0.36,0.36-0.36h2c0.199,0,0.36,0.161,0.36,0.36v2c0,0.199-0.161,0.36-0.36,0.36h-1.64V10 C28.36,10.199,28.199,10.36,28,10.36z M25.36,9.64h2.279V7.36H25.36V9.64z M28.36,6.64h1.279V5.36H28.36V6.64z M12,7.36H8 C7.801,7.36,7.64,7.199,7.64,7V3c0-0.199,0.161-0.36,0.36-0.36h4c0.199,0,0.36,0.161,0.36,0.36v4C12.36,7.199,12.199,7.36,12,7.36z M8.36,6.64h3.28V3.36H8.36V6.64z M21,3.36h-2c-0.199,0-0.36-0.161-0.36-0.36V1c0-0.199,0.161-0.36,0.36-0.36h2 c0.199,0,0.36,0.161,0.36,0.36v2C21.36,3.199,21.199,3.36,21,3.36z M19.36,2.64h1.279V1.36H19.36V2.64z"/></svg>',
 "gov": '<svg class="icon" fill="currentColor" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" aria-hidden="true" focusable="false"><path d="M16.023,31.355 c-5.518,0-10.821-2.985-13.56-8.101l-1.124,3.188l-0.679-0.24l1.526-4.329l4.329,1.576l-0.246,0.676l-3.134-1.141 c3.657,6.742,12.008,9.564,19.052,6.28c3.703-1.727,6.461-4.917,7.712-8.689c-0.615,0.858-1.409,1.596-2.351,2.162 c-1.8,1.082-3.91,1.397-5.949,0.89c-1.768-0.441-3.294-1.456-4.374-2.893l-0.831,3.332l-0.698-0.174l1.114-4.471l4.443,1.156 l-0.182,0.697l-3.152-0.82c0.973,1.223,2.312,2.089,3.854,2.473c1.854,0.465,3.771,0.175,5.404-0.808 c2.12-1.273,3.412-3.507,3.463-5.98c0-0.046,0-0.093,0-0.14L31.36,16c0,0.034-0.001,0.068-0.001,0.102h0.001 c-0.001,0.016-0.001,0.032-0.001,0.047c-0.062,5.886-3.53,11.279-8.868,13.767C20.397,30.894,18.193,31.355,16.023,31.355z M1.36,16 H0.64C0.644,10.056,4.125,4.593,9.508,2.083c3.718-1.734,7.888-1.917,11.746-0.513c3.585,1.305,6.498,3.836,8.283,7.174l1.123-3.186 l0.68,0.239l-1.526,4.329l-4.329-1.575l0.246-0.677l3.135,1.141c-1.704-3.148-4.465-5.534-7.858-6.769 c-3.673-1.338-7.65-1.164-11.194,0.489c-3.7,1.725-6.458,4.914-7.709,8.683c0.614-0.854,1.406-1.589,2.348-2.155 c3.477-2.088,7.936-1.167,10.323,2.003l0.831-3.333l0.698,0.174l-1.114,4.47l-4.443-1.156l0.182-0.697l3.152,0.82 c-0.973-1.223-2.312-2.088-3.854-2.472C8.375,8.609,6.457,8.897,4.823,9.88C2.657,11.181,1.362,13.469,1.36,16z"/></svg>',
}

# ---------------------------------------------------------------- content
T = {
"ar": {
 "dir": "rtl", "lang": "ar", "base": "/", "other": "en", "other_label": "English", "locale": "ar_SA", "other_locale": "en_US",
 "brand": "شركة إليفانتك", "brand_core": "إليفانتك", "co": "شركة", "skip": "انتقل إلى المحتوى", "home_label": "الرئيسية",
 "nav": [("about", "عن الشركة"), ("services", "خدماتنا"), ("projects", "خبراتنا"), ("team", "الفريق"), ("partners", "الشركاء"), ("contact", "تواصل معنا")],
 "nav_services": "خدماتنا",
 "title": "شركة إليفانتك | الذكاء الاصطناعي المؤسسي والذكاء الجيومكاني ودعم القرار للمحافظ والمشاريع في الرياض",
 "desc": "شركة إليفانتك شركة سعودية في الرياض تجمع حلول الذكاء الاصطناعي المؤسسي، والذكاء الاصطناعي الجيومكاني (GeoAI)، ودعم القرار للمحافظ والمشاريع لدعم برامج التحول الرقمي والبيئة في رؤية 2030.",
 "eyebrow": "الرياض · المملكة العربية السعودية",
 "h1": "نحوّل بياناتك المعقدة إلى قرارات تتحكم أنت بها",
 "lead": "الذكاء الاصطناعي المؤسسي والجيومكاني (GeoAI) ودعم القرار للمحافظ والمشاريع للجهات الحكومية والشركات والمنشآت الصغيرة والمتوسطة والمكاتب المهنية. نحوّل التعقيد إلى وضوح، والوضوح إلى أثر مستدام.",
 "cta1": "تواصل معنا", "cta2": "خدماتنا", "logo_alt": "شعار إليفانتك",
 "trust": ["شركة سعودية مسجلة في الرياض", "تصميم متوافق مع ضوابط NCA-ECC"],
 "partners_eyebrow": "", "partners_h": "الشركاء", "partner_role": "شريك استراتيجي", "partner_name": "Accelerate Consulting", "partner_p": "شركة استشارات أعمال وتأكيد مهني، تساعد المنظمات على تعزيز الحوكمة واتخاذ قرارات استراتيجية سليمة واعتماد حلول مبتكرة.", "partner_p2": "نتعاون معًا في تطوير حلّ متكامل للحوكمة وإدارة المخاطر والامتثال (GRC) للمنظمات في المملكة.", "partner_link": "زيارة الموقع",
 "about_eyebrow": "عن الشركة", "about_h": "الرؤية والرسالة",
 "vision_h": "رؤيتنا", "vision": "أن نكون الشريك الموثوق للرواد وأصحاب الأعمال في تمكين القرار، عبر حلول ذكية ومستدامة وفعّالة اقتصاديًا تتحول إلى محافظ منظّمة تقودها البيانات.",
 "mission_h": "رسالتنا", "mission": "نطوّر وننشر أنظمة ذكاء الأعمال بالذكاء الاصطناعي وحلول GeoAI وأنظمة دعم قرار للمحافظ والمشاريع، لتساعد الجهات السعودية على التعامل مع بياناتها بوصفها أصلًا استراتيجيًا. وبدمج الهندسة المتقدمة للذكاء الاصطناعي المؤسسي مع GeoAI وممارسات إدارة المحافظ والبرامج والمشاريع المعتمدة، نحوّل البيانات المعقدة إلى معلومات جاهزة لمجلس الإدارة.",
 "gap_h": "لماذا وُجدنا", "gap": "معظم الجهات تقدّم قطعة واحدة من الصورة. شركات الاستشارات الهندسية التقليدية تقدّم دراسات فنية ويبقى تتبّع المحافظ والمشاريع يدويًا، وشركات الذكاء الاصطناعي تبني النماذج دون فهم لعدم اليقين في البيانات البيئية والمكانية. نحن نجمع الأمور الثلاثة: دعم القرار للمحافظ والمشاريع، وGeoAI، والنشر التشغيلي للذكاء الاصطناعي، في كيان سعودي واحد.",
 "svc_more": "ما الذي يشمله", "svc_eyebrow": "خدماتنا", "svc_h": "ثلاث ركائز متكاملة",
 "pillars": [{'icon': 'ai', 'h': 'الذكاء الاصطناعي المؤسسي والتحول الرقمي', 'story': 'ذكاء اصطناعي يعمل لصالحك، وبياناتك تبقى تحت سيطرتك.', 'tags': ['الأتمتة', 'النشر السيادي', 'ذكاء المستندات'], 'outcome': 'أن تستفيد مؤسستك من إمكانات الذكاء الاصطناعي، دون التنازل عن التحكم أو الأمن أو الثقة.', 'items': [('وكلاء الذكاء الاصطناعي وأتمتة إجراءات العمل', 'تقليل العمل اليدوي في الموافقات والطلبات، مع بقاء القرار النهائي بيد فريقك.'), ('التحول الرقمي وتطوير نماذج العمل', 'خارطة طريق واضحة تحدد أين يضيف الذكاء الاصطناعي قيمة حقيقية، وكيف تتبنّاه فرقك.'), ('تطوير المنصات والتطبيقات الذكية', 'منصات وتطبيقات مصممة لاحتياجك، جاهزة للتشغيل والتوسع.'), ('إدارة المعرفة وذكاء المستندات', 'الوصول إلى أي معلومة في مستنداتك بالعربية والإنجليزية خلال ثوانٍ.'), ('حلول ذكاء اصطناعي خاصة ورائدة، وبياناتك داخل المملكة', 'تُشغَّل في مراكز بياناتك أو على سحابة سعودية، وفق ضوابط NCA-ECC وNDMO وإرشادات سدايا ونظام حماية البيانات الشخصية.')], 'work': []}, {'icon': 'geo', 'h': 'GeoAI والاستشارات المكانية', 'story': 'نفهم المكان، لنكشف ما وراء البيانات.', 'tags': ['تحليل صور الأقمار الصناعية', 'البنية المكانية للبيانات', 'التوائم الرقمية'], 'outcome': 'تحويل البيانات المكانية إلى معرفة قابلة للاستخدام، تساعد على فهم الواقع واستشراف المستقبل وإدارة الموارد بصورة أكثر كفاءة.', 'items': [('تحليلات GeoAI لصور الأقمار الصناعية والبيانات المكانية', 'نماذج تحلل صور الأقمار الصناعية وبيانات الاستشعار عن بعد لرصد التغيّر واكتشاف الأنماط.'), ('قواعد البيانات والبنية التحتية للبيانات المكانية', 'قواعد بيانات جيومكانية موحّدة وفق معايير NDMO، تكون مرجعًا واحدًا لكل الجهات المعنية.'), ('الذكاء المكاني والتشغيل الذكي', 'رؤية لحظية للأصول والعمليات الميدانية، لتتحرك فرقك في الوقت والمكان المناسبين.'), ('التوائم الرقمية للبنية التحتية', 'نسخة رقمية حيّة من أصولك تتيح اختبار القرارات قبل تنفيذها على الأرض.')], 'work': []}, {'icon': 'gov', 'h': 'دعم القرار واستشارات المحافظ', 'story': 'رؤية متكاملة تمنحك الوضوح والتحكم في قراراتك.', 'tags': ['لوحات حيّة', 'ممارسات معتمدة', 'برامج التحول'], 'outcome': 'أن تنتقل من متابعة التقارير إلى فهم الأداء، ومن رصد المشكلات إلى استباقها، ومن إدارة الأنشطة إلى تحقيق النتائج.', 'items': [('لوحات المعلومات والتحليلات التنفيذية', 'صورة واحدة محدّثة للتكلفة والجدول الزمني والمخاطر، بلغة يفهمها متخذ القرار.'), ('أنظمة متابعة المحافظ والبرامج والمشاريع', 'متابعة الأداء عبر كل المشاريع من مكان واحد، مع إنذار مبكر بالانحرافات.'), ('دعم القرار المبني على أفضل الممارسات المهنية', 'أنظمة يصممها خبراء حاصلون على اعتمادات PfMP وPgMP وPMP.'), ('دعم برامج التحول الرقمي', 'حوكمة ومتابعة برامج التحول من التخطيط حتى قياس الأثر.')], 'work': [('Accelerat 360', 'منصة للحوكمة وإدارة المخاطر والامتثال (GRC)، نطوّرها بالشراكة مع Accelerate Consulting.', 'https://accelerat360.ai/'), ('قريبًا: ProPerM', 'منصة لإدارة أداء المشاريع.', '')]}],
 "proj_eyebrow": "خبراتنا", "proj_h": "نماذج من خبراتنا",
 "proj_note": "تحافظ إليفانتك على السرية. تُشارك المراجع التفصيلية ودراسات الحالة مباشرة، بعد توقيع اتفاقيات السرية المناسبة. وتمثل الفئات أدناه الخبرة المجمّعة لقيادة الشركة وفرق شركائها.",
 "proj_cols": ("القطاع", "نوع المشروع", "دورنا"),
 "proj": [("الذكاء الاصطناعي المؤسسي (السعودية)", "وكلاء ذكاء اصطناعي لسير عمل الخدمات", "نشر تشغيلي للذكاء الاصطناعي"),
          ("أنظمة ذكاء اصطناعي مخصصة", "تطوير تطبيقات ذكاء اصطناعي متكاملة", "هندسة النظام ونشره"),
          ("أنظمة GeoAI مخصصة", "حلول GeoAI", "بناء النظام مع شريك التطوير"),
          ("التحول الرقمي", "برامج التحول الرقمي للشركات", "الاستشارات ودعم التنفيذ"),
          ("دعم القرار للمحافظ والمشاريع", "لوحات دعم قرار للمحافظ والمشاريع", "تصميم النظام وبناء اللوحات")],
 "team_eyebrow": "", "team_h": "الفريق",
 "team": [("م. خالد عبدالرحمن", "الرئيس التنفيذي", "خبرة تزيد على 15 عامًا في القطاعين الخاص والعام في الولايات المتحدة، في تسليم برمجيات المؤسسات والتحول الرقمي. يقود عمليات الشركة وشراكاتها الدولية في المملكة."),
          ("م. نزار قاضي", "استشاري تطوير الأعمال", "خبرة تزيد على 15 عامًا في الاستشارات المتعلقة باستراتيجية النمو والاستثمار، وتأسيس مكاتب إدارة المشاريع (PMO)، وقيادة الحوكمة وإدارة المخاطر والامتثال في القطاعين الحكومي والخاص. أدار محافظ كبرى من المشاريع الحكومية والاستثمارية."),
          ("د. محمد عبدالله", "المدير الفني", "خبرة تزيد على 20 عامًا في ألمانيا في الهيدروإنفورماتكس ونظم المعلومات الجغرافية (GIS) والبيانات الجيومكانية، وفي إدارة المحافظ والبرامج والمشاريع.")],
 "sme_h": "نخبة الخبراء المتخصصين", "sme_eyebrow": "",
 "sme": [("الذكاء الاصطناعي", "نماذج وتطبيقات الذكاء الاصطناعي المؤسسي، من التعلّم الآلي إلى النماذج اللغوية، مصممة لتعمل داخل ضوابط الأمن والامتثال لدى العميل."),
         ("GeoAI ونظم المعلومات الجغرافية والاستشعار عن بعد", "تحليلات الصور الجيومكانية وبيانات الأقمار الصناعية ونظم المعلومات الجغرافية (GIS)، لتحويل البيانات المكانية إلى رؤى قابلة للتنفيذ."),
         ("تطوير البرمجيات", "مطورون متخصصون في التطبيقات المتكاملة والواجهات والخدمات الخلفية، يسلّمون منصات جاهزة للإنتاج وقابلة للتوسع."),
         ("البنية المعمارية والحوسبة السحابية", "تصميم معماريات المؤسسات وحلول السحابة وإنترنت الأشياء، بما يدمج التقنيات الناشئة في بيئات حيوية."),
         ("الأمن السيبراني", "تطبيق نموذج انعدام الثقة (Zero Trust) واختبار الاختراق وحماية البنية التحتية والبيانات الحساسة."),
         ("إدارة المشاريع والبرامج", "إدارة المحافظ والبرامج والمشاريع وفق أفضل الممارسات المعتمدة، من التخطيط والحوكمة إلى التسليم وقياس النتائج."),
         ("تطوير الأعمال", "استراتيجية الدخول إلى السوق وتحديد الفرص وبناء الشراكات، لدعم نمو الشركات التقنية والمؤسسية في المملكة.")],
 "it_h": "الدعم الفني", "it_p": "للمساعدة في أي استفسار تقني، تواصل معنا على",
 "network": "يقود فريقنا الأساسي كل مشروع، ويُنفَّذ بدعم مهندسين ومحللين متخصصين في الذكاء الاصطناعي وتطوير التطبيقات المتكاملة والاستشعار عن بعد ونظم المعلومات الجغرافية، وخبراء في البيئة والبنية التحتية.",
 "why_eyebrow": "لماذا إليفانتك", "why_h": "الميزة السعودية",
 "why": [("شركة سعودية مسجلة ومقرها الرياض", "نعمل داخل بيئتكم التنظيمية وبيئة المشتريات."),
         ("متوافقون مع رؤية 2030", "يدعم عملنا مباشرة أهداف الاستدامة البيئية والتحول الرقمي."),
         ("نشر سيادي للذكاء الاصطناعي", "تصميم متوافق مع NCA-ECC ونظام حماية البيانات الشخصية، وقابل للنشر محليًا أو على سحابة خاصة، وهو حاسم للجهات الحكومية."),
         ("ثلاث كفاءات في مكان واحد", "دعم القرار للمحافظ والمشاريع، وGeoAI، والذكاء الاصطناعي المؤسسي في فريق واحد."),
         ("تنفيذ بلغتين", "العربية والإنجليزية، مع ملخصات تنفيذية تناسب صانع القرار السعودي."),],
 "contact_eyebrow": "تواصل معنا", "contact_h": "لنناقش مشروعك", "contact_p": "اكتب لنا عن احتياجك. يرد عليك فريقنا في الرياض وفرجينيا، وتُعامل جميع الاستفسارات بسرية تامة.",
 "book": "احجز مكالمة تشخيصية مدتها 30 دقيقة", "linkedin": "لينكدإن",
 "labels": {"email": "البريد الإلكتروني", "phone": "الهاتف", "hq": "الموقع", "hq_val": "حي العليا، الرياض، المملكة العربية السعودية", "cr": "السجل التجاري",
            "contact_h": "تواصل", "company_h": "الشركة", "privacy": "سياسة الخصوصية", "rights": "جميع الحقوق محفوظة", "links_h": "روابط"},
 "form": {"h": "أرسل لنا طلبك", "name": "الاسم", "org": "الجهة أو الشركة", "email": "البريد الإلكتروني", "phone": "الهاتف (اختياري)",
          "interest": "الخدمة المطلوبة", "msg": "رسالتك", "msg_ph": "اكتب هنا عن احتياجك أو المشروع الذي تعمل عليه.",
          "consent": "أوافق على استخدام بياناتي للرد على طلبي وفق", "send": "إرسال", "sending": "جارٍ الإرسال...",
          "ok": "وصلنا طلبك، وسنعود إليك قريبًا.", "err": "تعذر الإرسال. أرسل لنا على البريد مباشرة: " + EMAIL,
          "mail_note": "سيفتح الإرسال تطبيق البريد لديك برسالة جاهزة.", "req": "هذا الحقل مطلوب", "subject": "استفسار جديد من موقع إليفانتك",
          "opts": ["الذكاء الاصطناعي المؤسسي", "GeoAI", "دعم القرار للمحافظ والمشاريع", "أخرى"]},
 "privacy": {
  "title": "سياسة الخصوصية | شركة إليفانتك", "desc": "سياسة الخصوصية لشركة إليفانتك: كيف نتعامل مع البيانات التي تصلنا عبر البريد الإلكتروني ونموذج التواصل، وما الذي لا نجمعه، وكيف تمارس حقوقك.",
  "h1": "سياسة الخصوصية", "effective": "تاريخ السريان: نوفمبر 2026",
  "body": [
   ("1. من نحن", "تُشغّل شركة إليفانتك (الرياض، المملكة العربية السعودية) هذا الموقع والخدمات المرتبطة به. وتشير عبارتا «شركة إليفانتك» و«نحن» إلى هذه الجهة."),
   ("2. المعلومات التي نجمعها", "لا يستخدم هذا الموقع ملفات تعريف الارتباط ولا أدوات تحليل أو تتبع إعلاني، وتُقدَّم الخطوط والملفات من خادمنا نفسه لا من أطراف ثالثة. ومثل أي موقع، يسجّل مزوّد الاستضافة بيانات تقنية معتادة (مثل عنوان الشبكة والتاريخ والوقت والصفحة المطلوبة) لأغراض الأمان والتشغيل. وإذا راسلتنا عبر البريد الإلكتروني أو النموذج، فإننا نستلم الاسم وجهة العمل وبيانات التواصل ومضمون رسالتك."),
   ("3. كيف نستخدم معلوماتك", "نستخدم المعلومات التي تصلنا للرد على استفسارك وتقييم فرص التعاون وحفظ سجل المراسلات المؤسسية. ولا نبيع بياناتك الشخصية ولا نؤجرها ولا نشاركها مع أطراف ثالثة لأغراض تسويقية."),
   ("4. مكان معالجة البيانات", "تُعالج البيانات التي تصلنا عبر هذا الموقع وفق متطلبات نظام حماية البيانات الشخصية (PDPL) وإرشادات الهيئة السعودية للبيانات والذكاء الاصطناعي (سدايا) المعمول بها."),
   ("5. حقوقك", "يحق لك طلب الاطلاع على بياناتك الشخصية أو تصحيحها أو حذفها أو تقييد معالجتها وفق الأنظمة المعمول بها. لممارسة هذه الحقوق تواصل معنا على " + PRIVACY_EMAIL + "."),
   ("6. التواصل", "لأي استفسار عن الخصوصية راسلنا على " + PRIVACY_EMAIL + "."),
  ]},
 "news_eyebrow": "", "news_h": "الأخبار",
 "profile_h": "حمّل الملف التعريفي للشركة", "profile_p": "تعرّف على خدماتنا ومنهجنا وفريقنا في ملف تعريفي موجز بصيغة PDF.",
 "profile_ar": "الملف التعريفي (العربية)", "profile_en": "Company Profile (English)", "news_none": "ترقبوا أخبارنا قريبًا.",
 "nf_h": "الصفحة غير موجودة",
},
"en": {
 "dir": "ltr", "lang": "en", "base": "/en/", "other": "ar", "other_label": "العربية", "locale": "en_US", "other_locale": "ar_SA",
 "brand": "Elevantec Company", "brand_core": "elevantec", "co": "Company", "skip": "Skip to content", "home_label": "Home",
 "nav": [("about", "About"), ("services", "Services"), ("projects", "Experience"), ("team", "Team"), ("partners", "Partners"), ("contact", "Contact")],
 "nav_services": "Services",
 "title": "Elevantec Company | Enterprise AI, GeoAI and Portfolio and Project Decision Support in Riyadh",
 "desc": "Elevantec Company is a Saudi company in Riyadh combining enterprise AI deployment, GeoAI and portfolio and project decision support for Vision 2030 digital transformation and environmental programs.",
 "eyebrow": "Riyadh · Saudi Arabia",
 "h1": "Turn complex data into decisions you control.",
 "lead": "Enterprise AI, GeoAI and portfolio and project decision support for government, corporates, SMEs and professional firms. We turn complexity into clarity, and clarity into sustainable impact.",
 "cta1": "Contact us", "cta2": "Our services", "logo_alt": "Elevantec logo",
 "trust": ["Saudi-registered, Riyadh-based", "Designed to align with NCA-ECC"],
 "partners_eyebrow": "", "partners_h": "Partners", "partner_role": "Strategic partner", "partner_name": "Accelerate Consulting", "partner_p": "A business consulting and assurance firm that helps organizations strengthen governance, make sound strategic decisions and adopt innovative solutions.", "partner_p2": "Together, we are collaborating on a governance, risk and compliance (GRC) solution for organizations in the Kingdom.", "partner_link": "Visit website",
 "about_eyebrow": "About", "about_h": "Vision and mission",
 "vision_h": "Our vision", "vision": "To be the trusted partner of entrepreneurs and business owners in enabling decisions, through smart, sustainable and economically sound solutions that become organized, data-driven portfolios.",
 "mission_h": "Our mission", "mission": "We develop and deploy AI business-intelligence systems, GeoAI solutions and decision-support systems for portfolios and projects, helping Saudi organizations treat data as a strategic asset. By combining enterprise-grade AI engineering, GeoAI, and certified portfolio, program and project management practice, we turn complex data into boardroom-ready intelligence.",
 "gap_h": "Why we exist", "gap": "Most firms offer one piece of the puzzle. Traditional engineering consultancies deliver technical studies but leave portfolios and projects tracked by hand. Pure AI firms build models but do not understand real-world uncertainty in environmental and spatial data. We bring all three together under one Saudi-registered entity: portfolio and project decision support, GeoAI and operational AI deployment.",
 "svc_more": "See what’s included", "svc_eyebrow": "Services", "svc_h": "Three integrated pillars",
 "pillars": [{'icon': 'ai', 'h': 'Enterprise AI and digital transformation', 'story': 'AI that works for you, while your data stays under your control.', 'tags': ['Automation', 'Sovereign deployment', 'Document intelligence'], 'outcome': 'Your organization gets the full potential of AI without giving up control, security or trust.', 'items': [('AI agents and workflow automation', 'Less manual work on approvals and requests, with the final decision staying with your team.'), ('Digital transformation and operating models', 'A clear roadmap showing where AI adds real value, and how your teams adopt it.'), ('Intelligent platforms and applications', 'Platforms and apps built around your needs, ready to run and scale.'), ('Knowledge management and document intelligence', 'Find any information in your documents, in Arabic or English, within seconds.'), ('Private, leading AI solutions, with your data in the Kingdom', 'Run in your own data centers or on a Saudi cloud, in line with NCA-ECC, NDMO, SDAIA guidance and PDPL.')], 'work': []}, {'icon': 'geo', 'h': 'GeoAI and spatial advisory', 'story': 'We understand place, to reveal what lies beyond the data.', 'tags': ['Satellite analytics', 'Spatial data infrastructure', 'Digital twins'], 'outcome': 'Spatial data turned into usable knowledge that helps you understand the present, anticipate the future and manage resources more efficiently.', 'items': [('GeoAI analytics for satellite imagery and spatial data', 'Models that analyze satellite and remote-sensing data to detect change and spot patterns.'), ('Geospatial databases and spatial data infrastructure', 'Unified geospatial databases built to NDMO standards, one reference for every stakeholder.'), ('Spatial intelligence and smart operations', 'A real-time view of assets and field operations, so your teams act at the right time and place.'), ('Digital twins for infrastructure', 'A living digital copy of your assets, so you can test decisions before acting on the ground.')], 'work': []}, {'icon': 'gov', 'h': 'Decision support and portfolio advisory', 'story': 'An integrated view that gives you clarity and control over your decisions.', 'tags': ['Live dashboards', 'Certified practice', 'Transformation programs'], 'outcome': 'Move from tracking reports to understanding performance, from spotting problems to anticipating them, and from managing activities to achieving results.', 'items': [('Executive dashboards and analytics', 'One up-to-date picture of cost, schedule and risk, in the language decision-makers use.'), ('Portfolio, program and project tracking systems', 'Track performance across every project in one place, with early warning on deviations.'), ('Decision support built on professional best practice', 'Systems designed by experts certified in PfMP, PgMP and PMP.'), ('Digital transformation program support', 'Governance and tracking for transformation programs, from planning to impact measurement.')], 'work': [('Accelerat 360', 'A governance, risk and compliance (GRC) platform we are developing with Accelerate Consulting.', 'https://accelerat360.ai/'), ('Coming soon: ProPerM', 'a project performance management platform.', '')]}],
 "proj_eyebrow": "Experience", "proj_h": "Representative experience",
 "proj_note": "Elevantec prioritizes confidentiality. Specific organizational references and detailed case studies are shared directly under appropriate confidentiality agreements. The categories below represent the combined track record of our leadership and partner teams.",
 "proj_cols": ("Sector", "Project type", "Our role"),
 "proj": [("Enterprise AI (KSA)", "AI agents for service workflows", "Operational AI deployment"),
          ("Custom AI systems", "Full-stack AI application development", "System architecture and deployment"),
          ("Custom GeoAI systems", "GeoAI solutions", "System build with our development partner"),
          ("Digital transformation", "Digital transformation programs for companies", "Advisory and delivery support"),
          ("Portfolio and project decision support", "Decision-support dashboards for portfolios and projects", "System design and dashboard build")],
 "team_eyebrow": "", "team_h": "Team",
 "team": [("Eng. Khalid Abdelrahman", "CEO", "Over 15 years of experience across the private and public sectors in the United States, in enterprise software delivery and digital transformation. Leads the company’s operations and international partnerships in the Kingdom."),
          ("Eng. Nizar Kadi", "Business Development Consultant", "15+ years of experience advising on growth strategy and investment, establishing PMOs, and leading governance, risk and compliance across government and commercial sectors. Has managed large government and investment project portfolios."),
          ("Dr. Mohammed Abdallah", "Technical Director", "20+ years of experience in Germany in hydroinformatics, GIS and geospatial analytics, and in portfolio, program and project management.")],
 "sme_h": "SMEs Pool", "sme_eyebrow": "",
 "sme": [("Artificial intelligence", "Enterprise AI models and applications, from machine learning to language models, built to run inside the client’s security and compliance controls."),
         ("GeoAI, GIS and remote sensing", "Geospatial imagery analytics, satellite data and GIS, turning spatial data into insight that can be acted on."),
         ("Software development", "Specialist full-stack engineers delivering production-ready, scalable platforms, from interfaces to back-end services."),
         ("Architecture and cloud", "Enterprise architecture, cloud and IoT solutions that integrate emerging technologies into mission-critical environments."),
         ("Cybersecurity", "Zero Trust implementation, penetration testing and protection of critical infrastructure and sensitive data."),
         ("Project and program management", "Portfolio, program and project management aligned with recognized best practices, from planning and governance through delivery and benefits tracking."),
         ("Business development", "Go-to-market strategy, opportunity identification and partnership building to support growth in the Kingdom.")],
 "it_h": "IT support", "it_p": "For help with any technical inquiry, please contact us at",
 "network": "Every engagement is led by our core team and delivered with specialist engineers and analysts in AI, full-stack development, GIS and remote sensing, and infrastructure and environmental advisory.",
 "why_eyebrow": "Why Elevantec", "why_h": "The Saudi advantage",
 "why": [("Saudi-registered, Riyadh-based", "We operate inside your regulatory and procurement environment."),
         ("Vision 2030-aligned", "Our work directly supports environmental sustainability and digital transformation goals."),
         ("Sovereign AI deployment", "Designed to align with NCA-ECC and PDPL, and deployable on-premises or in private cloud. Critical for government clients."),
         ("Three competencies in one team", "Portfolio and project decision support, GeoAI and enterprise AI together."),
         ("Bilingual delivery", "Arabic and English, with executive summaries tailored for Saudi decision-makers."),],
 "contact_eyebrow": "Contact", "contact_h": "Let's discuss your project", "contact_p": "Tell us what you need. Our teams in Riyadh and Virginia will get back to you, and all inquiries are handled with strict confidentiality.",
 "book": "Book a 30-minute diagnostic call", "linkedin": "LinkedIn",
 "labels": {"email": "Email", "phone": "Phone", "hq": "Location", "hq_val": "Al Olaya, Riyadh, Saudi Arabia", "cr": "C.R. number",
            "contact_h": "Contact", "company_h": "Company", "privacy": "Privacy policy", "rights": "All rights reserved", "links_h": "Links"},
 "form": {"h": "Send us a message", "name": "Name", "org": "Organization", "email": "Email", "phone": "Phone (optional)",
          "interest": "Service of interest", "msg": "Your message", "msg_ph": "Tell us about your need or the project you are working on.",
          "consent": "I agree that my data is used to answer my request, as described in the", "send": "Send", "sending": "Sending...",
          "ok": "We received your message and will get back to you shortly.", "err": "Could not send. Please email us directly: " + EMAIL,
          "mail_note": "Sending opens your email app with a ready message.", "req": "This field is required", "subject": "New enquiry from the Elevantec website",
          "opts": ["Enterprise AI", "GeoAI", "Portfolio and project decision support", "Other"]},
 "privacy": {
  "title": "Privacy Policy | Elevantec Company", "desc": "Elevantec Company's privacy policy: how we handle data sent by email and through the contact form, what we do not collect, and how to exercise your rights.",
  "h1": "Privacy policy", "effective": "Effective: November 2026",
  "body": [
   ("1. Who we are", "Elevantec Company (Riyadh, Saudi Arabia) operates this website and its related services. References to \"Elevantec Company\" and \"we\" mean this entity."),
   ("2. Information we collect", "This website does not use cookies, analytics or advertising trackers, and its fonts and files are served from our own server, not third parties. Like any website, our hosting provider logs routine technical data (such as network address, date and time, and the page requested) for security and operations. If you write to us by email or the contact form, we receive your name, organization, contact details and the content of your message."),
   ("3. How we use your information", "We use the information we receive to answer your enquiry, assess collaboration opportunities and keep a record of business correspondence. We do not sell or rent your personal data, and we do not share it with third parties for marketing."),
   ("4. Where data is processed", "Data sent through this website is handled in line with the Personal Data Protection Law (PDPL) and applicable SDAIA guidance."),
   ("5. Your rights", "You may ask to access, correct, delete or restrict the processing of your personal data under applicable law. To exercise these rights, contact us at " + PRIVACY_EMAIL + "."),
   ("6. Contact", "For any privacy question, write to " + PRIVACY_EMAIL + "."),
  ]},
 "news_eyebrow": "", "news_h": "News",
 "profile_h": "Download our company profile", "profile_p": "Learn about our services, approach and team in a concise PDF profile.",
 "profile_ar": "Company Profile (Arabic)", "profile_en": "Company Profile (English)", "news_none": "Stay tuned for our news.",
 "nf_h": "Page not found",
},
}

CONTENT_V2 = {"ar": {'slogan': 'رؤية أوضح. قرارات أفضل. أثر مستدام.', 'h1': 'من التعقيد إلى الوضوح، ومن الرؤية إلى الأثر.', 'lead': 'نضع الذكاء الاصطناعي والبيانات والتحليل الجيومكاني في خدمة قرارات أفضل ومشاريع أكثر نجاحًا. للجهات الحكومية، والقطاعات الخاضعة للتنظيم مثل المالية والصحة والطاقة، والشركات النامية.', 'pillars_line': ['الذكاء الاصطناعي المؤسسي', 'GeoAI', 'دعم القرار واستشارات المحافظ'], 'cta_book': 'احجز استشارة', 'cta_profile': 'حمّل الملف التعريفي', 'trust': [('location', 'شركة سعودية مقرها الرياض.'), ('sovereign-cloud', 'نستضيف بياناتك داخل المملكة.'), ('compliance', 'حلول متوافقة مع NCA-ECC وNDMO وهيئة الحكومة الرقمية ونظام حماية البيانات الشخصية.'), ('growth', 'نساهم في تعزيز المحتوى المحلي ونقل المعرفة، دعمًا لمستهدفات رؤية المملكة 2030.')], 'svc_h': 'من البيانات إلى القرار، بأمان وبالعربية أولًا.', 'svc_intro1': 'تملك مؤسستك اليوم بيانات أكثر من أي وقت مضى، لكن الوصول إلى قرار واضح وسريع ما زال تحديًا.', 'svc_intro2': 'نساعد الجهات الحكومية والشركات والمنشآت على توظيف الذكاء الاصطناعي والبيانات والتحليل الجيومكاني، وتطوير أنظمة ذكية لدعم القرار وتحسين الأداء، ضمن بيئات آمنة وسيادية تتوافق مع ضوابط الهيئة الوطنية للأمن السيبراني (NCA-ECC) ونظام حماية البيانات الشخصية، ومعايير مكتب إدارة البيانات الوطنية (NDMO) وهيئة الحكومة الرقمية (DGA)، مع استضافة البيانات داخل المملكة.', 'how_h': 'كيف نعمل', 'how': ['فهم التحدي', 'تصميم الحل', 'التنفيذ', 'قياس الأثر'], 'pillars_intro': 'نعمل من خلال ثلاث ركائز متكاملة:', 'outcome_label': 'النتيجة', 'work_h': 'من أعمالنا', 'why_h2': 'لماذا إليفانتك؟', 'contact_p': 'اكتب لنا عن احتياجك. يرد عليك فريقنا في الرياض، وتُعامل جميع الاستفسارات بسرية تامة.'},
 "en": {'slogan': 'Clearer vision. Better decisions. Lasting impact.', 'h1': 'From complexity to clarity, from vision to impact.', 'lead': 'We put AI, data and geospatial analytics to work for better decisions and more successful projects. For government entities, regulated sectors such as finance, health and energy, and growing companies.', 'pillars_line': ['Enterprise AI', 'GeoAI', 'Decision support and portfolio advisory'], 'cta_book': 'Book a consultation', 'cta_profile': 'Download the company profile', 'trust': [('location', 'A Saudi company headquartered in Riyadh.'), ('sovereign-cloud', 'We host your data inside the Kingdom.'), ('compliance', 'Solutions aligned with NCA-ECC, NDMO, the Digital Government Authority and PDPL.'), ('growth', 'We build local content and transfer knowledge, in support of Saudi Vision 2030.')], 'svc_h': 'From data to decision, securely and Arabic-first.', 'svc_intro1': 'Your organization has more data than ever, yet reaching a clear, fast decision is still a challenge.', 'svc_intro2': 'We help government entities, companies and organizations put AI, data and geospatial analytics to work, and build intelligent systems that support decisions and improve performance. Everything runs in secure, sovereign environments aligned with the National Cybersecurity Authority controls (NCA-ECC), the Personal Data Protection Law (PDPL), and the standards of the National Data Management Office (NDMO) and the Digital Government Authority (DGA), with data hosted inside the Kingdom.', 'how_h': 'How we work', 'how': ['Understand the challenge', 'Design the solution', 'Deliver', 'Measure the impact'], 'pillars_intro': 'We work through three integrated pillars:', 'outcome_label': 'Outcome', 'work_h': 'Our work', 'why_h2': 'Why Elevantec?', 'contact_p': 'Tell us what you need. Our team in Riyadh will get back to you, and all inquiries are handled with strict confidentiality.'}}
for _l in T: T[_l].update(CONTENT_V2[_l])
for _l in T: T[_l]["why"] = [T[_l]["why"][i] for i in (3, 2, 0, 1, 4)]   # display order

# ---------------------------------------------------------------- helpers
def esc(s): return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")
def path_for(lang, key):
    base = T[lang]["base"]; return base if key == "home" else f"{base}{key}/"
def url(lang, key): return SITE + path_for(lang, key)
def write(rel, content):
    p = os.path.join(ROOT, rel); os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w", encoding="utf-8").write(content)

def org_ld(lang):
    d = {"@context": "https://schema.org", "@type": "Organization", "name": "Elevantec Company", "alternateName": "شركة إليفانتك",
         "url": SITE + "/", "logo": SITE + "/assets/img/icon-512.png", "email": EMAIL,
         "address": {"@type": "PostalAddress", "addressLocality": "Riyadh", "addressCountry": "SA"}, "areaServed": "SA"}
    if PHONE_TEL: d["telephone"] = PHONE_TEL
    if CR: d["identifier"] = CR
    if LINKEDIN_URL: d["sameAs"] = [LINKEDIN_URL]
    return d

def head(lang, key, title, desc, ld=None):
    t = T[lang]; o = t["other"]
    ldh = "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>\n' for x in (ld or []))
    return f'''<!doctype html>
<html lang="{t["lang"]}" dir="{t["dir"]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{url(lang, key)}">
<link rel="alternate" hreflang="{lang}" href="{url(lang, key)}">
<link rel="alternate" hreflang="{o}" href="{url(o, key)}">
<link rel="alternate" hreflang="x-default" href="{url('ar', key)}">
<meta name="theme-color" content="#0b1b2b">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{esc(t["brand"])}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{url(lang, key)}">
<meta property="og:image" content="{SITE}/assets/img/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="{t["locale"]}">
<meta property="og:locale:alternate" content="{t["other_locale"]}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(desc)}">
<meta name="twitter:image" content="{SITE}/assets/img/og-image.png">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="/assets/img/favicon-32.png">
<link rel="apple-touch-icon" href="/assets/img/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
{PRELOAD[lang]}<link rel="stylesheet" href="{CSS}">
<script>document.documentElement.classList.add("js")</script>
{ldh}</head>
'''

MENU = {"ar": ("القائمة", "إغلاق القائمة"), "en": ("Menu", "Close menu")}

def header(lang, key):
    t = T[lang]; b = t["base"]; o = t["other"]
    links = "".join(f'<a href="{path_for(lang, k)}"' + (' aria-current="page"' if key == k else "") + f'>{n}</a>' for k, n in t["nav"])
    return f'''<a class="skip" href="#main">{t["skip"]}</a>
<header class="site">
  <a class="brand" href="{b}" aria-label="{esc(t["brand"])} - {t["home_label"]}"><img src="/assets/img/logo-h-en.svg" alt="" width="161" height="36"></a>
  <button class="menu-btn" type="button" hidden aria-label="{MENU[lang][0]}" aria-expanded="false" aria-controls="site-nav" data-open="{MENU[lang][0]}" data-close="{MENU[lang][1]}"><span class="bars" aria-hidden="true"></span></button>
  <nav class="main" id="site-nav" aria-label="{'التنقل الرئيسي' if lang == 'ar' else 'Main'}">
    {links}
    <a class="lang" href="{path_for(o, key)}" hreflang="{o}" lang="{o}">{t["other_label"]}</a>
  </nav>
</header>
'''

LI_SVG = '<svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true" fill="currentColor"><path d="M20.45 20.45h-3.56v-5.57c0-1.33-.03-3.04-1.85-3.04-1.86 0-2.14 1.45-2.14 2.94v5.67H9.34V9h3.41v1.56h.05c.48-.9 1.64-1.85 3.37-1.85 3.6 0 4.27 2.37 4.27 5.45v6.29zM5.34 7.43a2.06 2.06 0 1 1 0-4.12 2.06 2.06 0 0 1 0 4.12zM7.12 20.45H3.56V9h3.56v11.45zM22.22 0H1.77C.79 0 0 .77 0 1.73v20.54C0 23.23.79 24 1.77 24h20.45c.98 0 1.78-.77 1.78-1.73V1.73C24 .77 23.2 0 22.22 0z"/></svg>'

def contact_items(lang):
    t = T[lang]; L = t["labels"]; rows = [(L["email"], f'<a href="mailto:{EMAIL}"><bdi>{EMAIL}</bdi></a>')]
    if PHONE_TEL: rows.append((L["phone"], f'<a href="tel:{PHONE_TEL}"><bdi>{PHONE_DISPLAY}</bdi></a>'))
    if LINKEDIN_URL: rows.append((t["linkedin"], f'<a href="{LINKEDIN_URL}" target="_blank" rel="noopener">LinkedIn</a>'))
    rows.append((L["hq"], L["hq_val"]))
    if CR: rows.append((L["cr"], f"<bdi>{CR}</bdi>"))
    return rows

def footer(lang):
    t = T[lang]; L = t["labels"]; b = t["base"]
    nav = "".join(f'<li><a href="{path_for(lang, k)}">{n}</a></li>' for k, n in t["nav"][:-1])
    contact = "".join(f"<li>{v}</li>" for k, v in contact_items(lang) if k != L["cr"] and k != t["linkedin"])
    social = f'<p class="social"><a href="{LINKEDIN_URL}" target="_blank" rel="noopener" aria-label="LinkedIn">{LI_SVG}</a></p>' if LINKEDIN_URL else ""
    return f'''<footer class="site">
  <div class="wrap">
    <div class="stack g12"><a class="brand" href="{b}" aria-label="{esc(t["brand"])}"><img src="/assets/img/logo-h-en.svg" alt="" width="134" height="30" loading="lazy"></a>
      <p>{L["hq_val"]}</p>{social}</div>
    <div><h2>{L["links_h"]}</h2><ul>{nav}</ul></div>
    <div><h2>{L["contact_h"]}</h2><ul>{contact}</ul></div>
    <div><h2>{L["company_h"]}</h2><ul>{"<li>" + L["cr"] + ": <bdi>" + CR + "</bdi></li>" if CR else ""}<li><a href="{path_for(lang, "privacy")}">{L["privacy"]}</a></li></ul></div>
    <p class="fine">© 2026 {esc(t["brand"])}. {L["rights"]}.</p>
  </div>
</footer>
'''

def form_html(lang):
    f = T[lang]["form"]; t = T[lang]
    opts = "".join(f'<option value="{esc(o)}">{o}</option>' for o in f["opts"])
    action = FORM_ENDPOINT or f"mailto:{EMAIL}"
    nf = ' name="contact" data-netlify="true" netlify-honeypot="_gotcha"' if FORM_ENDPOINT == "/" else ""
    nf_hidden = f'<input type="hidden" name="form-name" value="contact"><input type="hidden" name="subject" value="{esc(f["subject"])}">' if FORM_ENDPOINT == "/" else ""
    return f'''<form class="form" id="f-home"{nf} method="post" action="{action}" data-endpoint="{FORM_ENDPOINT}" data-key="{FORM_KEY}" data-subject="{esc(f["subject"])}" data-ok="{esc(f["ok"])}" data-err="{esc(f["err"])}" data-sending="{esc(f["sending"])}" data-req="{esc(f["req"])}" novalidate>
  {nf_hidden}<h2>{f["h"]}</h2>
  <div class="fields">
    <label for="f-name">{f["name"]}<input id="f-name" name="name" type="text" autocomplete="name" required></label>
    <label for="f-org">{f["org"]}<input id="f-org" name="organization" type="text" autocomplete="organization"></label>
    <label for="f-email">{f["email"]}<input id="f-email" name="email" type="email" autocomplete="email" dir="ltr" required></label>
    <label for="f-phone">{f["phone"]}<input id="f-phone" name="phone" type="tel" autocomplete="tel" dir="ltr"></label>
    <label for="f-int" class="full">{f["interest"]}<select id="f-int" name="division">{opts}</select></label>
    <label for="f-msg" class="full">{f["msg"]}<textarea id="f-msg" name="message" rows="5" placeholder="{esc(f["msg_ph"])}" required></textarea></label>
  </div>
  <input class="hp" type="text" name="_gotcha" tabindex="-1" autocomplete="off" aria-hidden="true">
  <label class="consent" for="f-ok"><input id="f-ok" name="consent" type="checkbox" required><span>{f["consent"]} <a href="{path_for(lang, "privacy")}">{t["labels"]["privacy"]}</a></span></label>
  <div class="actions"><button class="btn gold" type="submit">{f["send"]}</button>{'' if FORM_ENDPOINT else '<p class="note">' + f["mail_note"] + '</p>'}</div>
  <p class="status" role="status" aria-live="polite"></p>
</form>'''

# ---------------------------------------------------------------- pages
PAGES = ["about", "services", "projects", "team", "partners", "news", "contact"]
GO = {
 "ar": {"about": "رؤيتنا ورسالتنا، ولماذا نجمع دعم القرار للمحافظ والمشاريع وGeoAI والذكاء الاصطناعي المؤسسي في فريق واحد.",
        "services": "ثلاث ركائز متكاملة: الذكاء الاصطناعي المؤسسي، والاستشارات في GeoAI، ودعم القرار للمحافظ والمشاريع.",
        "projects": "فئات المشاريع التي نعمل فيها ودورنا في كل منها.",
        "team": "قيادة الشركة وشبكة الخبراء التي تدعمها.", "news": "أخبار الشركة والملف التعريفي.", "partners": "الشركات التي نعمل معها لتقديم حلول متكاملة.",
        "contact": "اكتب لنا عن مشروعك.", "more": "اعرف المزيد", "explore_h": "استكشف إليفانتك"},
 "en": {"about": "Our vision and mission, and why we bring portfolio and project decision support, GeoAI and enterprise AI into one team.",
        "services": "Three integrated pillars: enterprise AI, GeoAI advisory, and portfolio and project decision support.",
        "projects": "The project categories we work in and our role in each.",
        "team": "The company's leadership and the expert network behind it.", "news": "Company news and our company profile.", "partners": "The companies we work with to deliver integrated solutions.",
        "contact": "Tell us about your project.", "more": "Learn more", "explore_h": "Explore Elevantec"},
}

def sec_partners(t):
    return f'''<section class="partners"><div class="wrap stack g28">
<div class="card partner"><div class="plogo"><img src="/assets/img/accelerat-logo.png" alt="Accelerat" width="1800" height="265" loading="lazy"></div>
<div class="pbody"><p class="eyebrow">{t["partner_role"]}</p><h3><bdi>{t["partner_name"]}</bdi></h3><p class="muted">{t["partner_p"]}</p><p class="muted">{t["partner_p2"]}</p><a class="more" href="https://accelerateconsulting.net/" target="_blank" rel="noopener">{t["partner_link"]} ↗</a></div></div></div></section>
'''

def sec_about(t):
    why = "".join(f'<div class="card why4">{CICON(i)}<p>{esc(x)}</p></div>' for i, x in t["trust"])
    return f'''<section class="alt"><div class="wrap stack g48">
  <div class="cols"><div class="stack g12"><h2 style="font-size:28px">{t["vision_h"]}</h2><p class="muted">{t["vision"]}</p></div><div class="stack g12"><h2 style="font-size:28px">{t["mission_h"]}</h2><p class="muted">{t["mission"]}</p></div></div>
  <div class="stack g12 gap-note"><h3>{t["gap_h"]}</h3><p class="muted">{t["gap"]}</p></div>
</div></section>
<section><div class="wrap stack g48">
  <div class="stack g12" style="max-width:640px"><h2>{t["why_h2"]}</h2></div>
  <div class="why4s">{why}</div>
</div></section>
'''

def sec_services(t, lang):
    cards = outs = ""
    for p in t["pillars"]:
        tags = "".join(f"<li>{esc(x)}</li>" for x in p["tags"])
        items = "".join(f"<li><b>{esc(h)}</b><span>{esc(d)}</span></li>" for h, d in p["items"])
        work = ""
        if p.get("work"):
            w = "".join((f'<li><a href="{u}" target="_blank" rel="noopener"><b><bdi>{esc(n)}</bdi></b></a>: <span>{esc(d)}</span></li>' if u else f'<li><b>{esc(n)}</b>{"، " if lang == "ar" else ", "}<span>{esc(d)}</span></li>') for n, d, u in p["work"])
            work = f'<div class="work-list"><p class="wl-h">{t["work_h"]}</p><ul>{w}</ul></div>'
        cards += f'''<div class="card pcard">{ICONS[p["icon"]]}<h2>{esc(p["h"])}</h2><p class="story">{esc(p["story"])}</p><ul class="tags">{tags}</ul>
<details><summary>{t["svc_more"]}</summary><ul class="incl">{items}</ul></details>{work}</div>
'''
        outs += f'<div><p class="ol">{t["outcome_label"]}</p><p>{esc(p["outcome"])}</p></div>'
    how = "".join(f'<li><em>0{i+1}</em><span>{esc(x)}</span></li>' for i, x in enumerate(t["how"]))
    first, second = (("ar", "profile_ar"), ("en", "profile_en")) if lang == "ar" else (("en", "profile_en"), ("ar", "profile_ar"))
    return f'''<section class="svc-intro"><div class="wrap stack g28"><div class="stack g20" style="max-width:78ch"><p class="lead2">{t["svc_intro1"]}</p><p class="muted">{t["svc_intro2"]}</p></div>
<div class="how"><p class="how-h">{t["how_h"]}</p><ol>{how}</ol></div></div></section>
<section><div class="wrap stack g48"><h2 class="pi">{t["pillars_intro"]}</h2><div class="pcards">{cards}</div><div class="outcomes">{outs}</div>
<div class="btns svc-cta"><a class="btn gold" href="{path_for(lang, "contact")}">{t["cta_book"]}</a><a class="btn" href="{PROFILE[first[0]]}" download>{t["cta_profile"]}</a></div></div></section>
'''

def sec_projects(t):
    c = t["proj_cols"]
    proj = "".join(f'<div class="card"><p class="eyebrow">{esc(a)}</p><h2>{esc(b)}</h2></div>' for a, b, r in t["proj"])
    return f'<section><div class="wrap stack g48"><p class="muted" style="max-width:72ch">{t["proj_note"]}</p><div class="cards">{proj}</div></div></section>\n'

def sec_team(t):
    team = ""
    PERSONAL = ["k.abdelrahman@elevantec.sa", "n.kadi@elevantec.sa", "m.abdallah@elevantec.sa"]
    PHOTOS = ["khalid", "nizar", "mohammed"]
    PHONES = {1: ("+966592805555", "+966 59 280 5555")}
    CREDS = [["CISA"], ["P3O", "PMP", "PMI-RMP", "GRCP", "OKR"], ["PfMP", "PgMP", "PMP", "PMOCP", "PBA"]]
    for i, (n, r, note) in enumerate(t["team"]):
        em = (PERSONAL[i] if i < len(PERSONAL) else None) or EMAIL
        photo = f'<img class="avatar" src="/assets/img/team/{PHOTOS[i]}.jpg" alt="{esc(n)}" width="320" height="320" loading="lazy">' if i < len(PHOTOS) else ""
        lines = []
        tel, disp = PHONES.get(i, (PHONE_TEL, PHONE_DISPLAY))
        if tel: lines.append(f'<li><a href="tel:{tel}">{CICON("phone","cicon ci")}<bdi>{disp}</bdi></a></li>')
        lines.append(f'<li><a href="mailto:{em}">{CICON("mail","cicon ci")}<bdi>{em}</bdi></a></li>')
        team += f'<div class="card person">{photo}<div class="pbody"><h2>{esc(n)}</h2><p class="role">{esc(r)}</p><ul class="creds" dir="ltr">{"".join(f"<li>{c}</li>" for c in (CREDS[i] if i < len(CREDS) else []))}</ul><p class="muted">{esc(note)}</p><ul>{"".join(lines)}</ul></div></div>\n'
    sme = "".join(f'<div class="card"><h3>{esc(n)}</h3><p class="muted">{esc(d)}</p></div>' for n, d in t["sme"])
    it = f'<div class="card it"><h2>{t["it_h"]}</h2><p class="muted">{t["it_p"]} <a href="mailto:{SUPPORT_EMAIL}"><bdi>{SUPPORT_EMAIL}</bdi></a>.</p></div>'
    return f'''<section><div class="wrap stack g48"><div class="people">{team}</div></div></section>
<section class="alt"><div class="wrap stack g48"><div class="stack g12" style="max-width:70ch">{("<p class=\"eyebrow\">" + t["sme_eyebrow"] + "</p>") if t["sme_eyebrow"] else ""}<h2>{t["sme_h"]}</h2><p class="muted">{t["network"]}</p></div><div class="cards sme">{sme}</div></div></section>
<section><div class="wrap">{it}</div></section>
'''

PROFILE = {"ar": "/files/Elevantec-Company-Profile-AR.pdf", "en": "/files/Elevantec-Company-Profile-EN.pdf"}
def sec_profile(lang, t):
    first, second = (("ar", "profile_ar"), ("en", "profile_en")) if lang == "ar" else (("en", "profile_en"), ("ar", "profile_ar"))
    btns = "".join(f'<a class="btn{" gold" if i == 0 else ""}" href="{PROFILE[l]}" download>{t[k]}</a>' for i, (l, k) in enumerate((first, second)))
    return f'''<section><div class="wrap"><div class="card profile"><h2>{t["profile_h"]}</h2><p class="muted">{t["profile_p"]}</p><div class="btns">{btns}</div></div></div></section>
'''

def sec_news(lang, t):
    first, second = (("ar", "profile_ar"), ("en", "profile_en")) if lang == "ar" else (("en", "profile_en"), ("ar", "profile_ar"))
    btns = "".join(f'<a class="btn{" gold" if i == 0 else ""}" href="{PROFILE[l]}" download>{t[k]}</a>' for i, (l, k) in enumerate((first, second)))
    return f'''<section><div class="wrap stack g48"><div class="card profile"><h2>{t["profile_h"]}</h2><p class="muted">{t["profile_p"]}</p><div class="btns">{btns}</div></div>
<p class="muted">{t["news_none"]}</p></div></section>
'''

def sec_contact(lang, t):
    rows = "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in contact_items(lang))
    book = f'<div class="btns"><a class="btn" href="{BOOKING_URL}" target="_blank" rel="noopener">{t["book"]}</a></div>' if BOOKING_URL else ""
    return f'''<section><div class="wrap cols">
    <div class="stack g28"><p class="muted">{t["contact_p"]}</p><dl class="rows">{rows}</dl>{book}</div>
    {form_html(lang)}
  </div></section>
'''

HEAD = {"about": ("about_eyebrow", "about_h"), "services": ("svc_eyebrow", "svc_h"), "projects": ("proj_eyebrow", "proj_h"),
        "team": ("team_eyebrow", "team_h"), "partners": ("partners_eyebrow", "partners_h"), "news": ("news_eyebrow", "news_h"), "contact": ("contact_eyebrow", "contact_h")}
SUB = {"services": "svc_h"}

def page(lang, key):
    t = T[lang]; eb, hh = HEAD[key]
    sec = {"about": lambda: sec_about(t), "services": lambda: sec_services(t, lang), "projects": lambda: sec_projects(t),
           "team": lambda: sec_team(t), "partners": lambda: sec_partners(t), "news": lambda: sec_news(lang, t), "contact": lambda: sec_contact(lang, t)}[key]()
    title = f'{(t["nav_services"] if key in SUB else t[hh])} | {t["brand"]}'
    desc = {"about": t["vision"], "services": t["gap"][:0] + GO[lang]["services"], "projects": GO[lang]["projects"],
            "team": GO[lang]["team"], "partners": GO[lang]["partners"], "news": GO[lang]["news"], "contact": t["contact_p"]}[key]
    crumb = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": t["home_label"], "item": url(lang, "home")},
        {"@type": "ListItem", "position": 2, "name": t["nav_services"] if key in SUB else t[hh], "item": url(lang, key)}]}
    body = f'''<body>
{header(lang, key)}<main id="main">
<section class="page-hero"><div class="wrap stack g20"><nav class="crumbs" aria-label="breadcrumb"><a href="{t["base"]}">{t["home_label"]}</a><span aria-hidden="true">/</span><span>{t["nav_services"] if key in SUB else t[hh]}</span></nav>{('<p class="eyebrow">' + t[eb] + '</p>') if t[eb] else ''}<h1>{t["nav_services"] if key in SUB else t[hh]}</h1>{('<p class="lead">' + t[SUB[key]] + '</p>') if key in SUB else ''}</div></section>
{sec}</main>
{footer(lang)}<script src="{JS}" defer></script>
</body></html>
'''
    return head(lang, key, title, desc, [crumb]) + body

def home(lang):
    t = T[lang]; g = GO[lang]
    arrow = "←" if lang == "ar" else "→"
    trust = "".join(f"<li>{CICON(i)}<span>{esc(x)}</span></li>" for i, x in t["trust"])
    pline = '<span aria-hidden="true">|</span>'.join(f"<span>{esc(x)}</span>" for x in t["pillars_line"])
    logo = "/assets/img/logo-en.png"   # same English logo on both language versions
    dims = (221, 350)
    names = dict(t["nav"])
    cards = "".join(f'<div class="card link"><h3>{names[k]}</h3><p>{g[k]}</p><a class="more stretch" href="{path_for(lang, k)}">{g["more"]} {arrow}</a></div>' for k in PAGES[:4])
    body = f'''<body>
{header(lang, "home")}<main id="main">
<section class="hero">
  <div class="wrap cols" style="align-items:center">
    <div class="stack g28">
      <p class="eyebrow slogan">{t["slogan"]}</p>
      <h1>{t["h1"]}</h1>
      <p class="lead">{t["lead"]}</p>
      <p class="pline">{pline}</p>
      <div class="btns"><a class="btn gold" href="{path_for(lang, "contact")}">{t["cta_book"]}</a><a class="btn" href="{path_for(lang, "services")}">{t["cta2"]}</a></div>
    </div>
    <div class="hero-art"><div class="emb"><img src="{logo}" alt="{t["logo_alt"]}" width="{dims[0]}" height="{dims[1]}" fetchpriority="high"><span class="sheen" style="--m:url({logo})" aria-hidden="true"></span></div></div>
  </div>
</section>
<section class="trustbar"><div class="wrap"><h2 class="vh">{t["why_h2"]}</h2><ul>{trust}</ul></div></section>
<section><div class="wrap stack g48"><h2>{g["explore_h"]}</h2><div class="cards">{cards}</div></div></section>
{sec_profile(lang, t)}
<section class="alt cta"><div class="wrap"><div class="stack g12"><h2>{t["contact_h"]}</h2><p class="muted">{g["contact"]}</p></div><div class="btns"><a class="btn gold" href="{path_for(lang, "contact")}">{t["cta_book"]}</a></div></div></section>
</main>
{footer(lang)}<script src="{JS}" defer></script>
</body></html>
'''
    return head(lang, "home", t["title"], t["desc"], [org_ld(lang)]) + body

def privacy(lang):
    t = T[lang]; p = t["privacy"]
    paras = "".join(f"<h2>{a}</h2><p>{c}</p>" for a, c in p["body"])
    crumb = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": t["home_label"], "item": url(lang, "home")},
        {"@type": "ListItem", "position": 2, "name": t["labels"]["privacy"], "item": url(lang, "privacy")}]}
    body = f'''<body>
{header(lang, "privacy")}<main id="main">
<section class="page-hero"><div class="wrap stack g20"><h1>{p["h1"]}</h1><p class="muted">{p["effective"]}</p></div></section>
<section><div class="wrap prose">{paras}</div></section>
</main>
{footer(lang)}<script src="{JS}" defer></script>
</body></html>
'''
    return head(lang, "privacy", p["title"], p["desc"], [crumb]) + body

def notfound():
    return f'''<!doctype html>
<html lang="ar" dir="rtl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>الصفحة غير موجودة | Page not found</title><meta name="robots" content="noindex">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="preload" href="/assets/fonts/ibm-plex-sans-arabic-arabic-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{CSS}"></head>
<body><main id="main" style="min-height:100vh;display:flex;align-items:center;justify-content:center;text-align:center;padding:40px 20px">
<div class="stack g20" style="align-items:center"><img src="/assets/img/mark.svg" alt="" width="56" height="88">
<h1 style="font-size:44px">الصفحة غير موجودة</h1><p class="muted">Page not found</p>
<div class="btns" style="justify-content:center"><a class="btn gold" href="/">الرئيسية</a><a class="btn" href="/en/">Home (English)</a></div></div></main></body></html>
'''

def sitemap():
    out = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for lang in ("ar", "en"):
        for k in ["home"] + [p for p in PAGES if p != "news"] + ["privacy"]:
            o = T[lang]["other"]
            out.append(f'<url><loc>{url(lang, k)}</loc><xhtml:link rel="alternate" hreflang="{lang}" href="{url(lang, k)}"/>'
                       f'<xhtml:link rel="alternate" hreflang="{o}" href="{url(o, k)}"/><xhtml:link rel="alternate" hreflang="x-default" href="{url("ar", k)}"/></url>')
    out.append("</urlset>")
    return "\n".join(out) + "\n"

if __name__ == "__main__":
    for lang in ("ar", "en"):
        b = T[lang]["base"].lstrip("/")
        write(f"{b}index.html", home(lang))
        for k in PAGES: write(f"{b}{k}/index.html", page(lang, k))
        write(f"{b}privacy/index.html", privacy(lang))
    write("404.html", notfound())
    write("sitemap.xml", sitemap())
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
    write("site.webmanifest", json.dumps({"name": "Elevantec Company | شركة إليفانتك", "short_name": "Elevantec", "start_url": "/", "display": "browser",
        "background_color": "#0b1b2b", "theme_color": "#0b1b2b",
        "icons": [{"src": "/assets/img/icon-192.png", "sizes": "192x192", "type": "image/png"}, {"src": "/assets/img/icon-512.png", "sizes": "512x512", "type": "image/png"}]}, ensure_ascii=False, indent=2) + "\n")
    write("_headers", """/*
  X-Content-Type-Options: nosniff
  X-Frame-Options: DENY
  Referrer-Policy: strict-origin-when-cross-origin
  Permissions-Policy: camera=(), microphone=(), geolocation=()
  Strict-Transport-Security: max-age=31536000; includeSubDomains
  Content-Security-Policy: default-src 'self'; style-src 'self'; font-src 'self'; img-src 'self' data:; script-src 'self' 'unsafe-inline'; script-src-attr 'none'; base-uri 'self'; form-action 'self' mailto: https://formspree.io https://api.web3forms.com; connect-src 'self' https://formspree.io https://api.web3forms.com; frame-ancestors 'none'; object-src 'none'
/assets/*
  Cache-Control: public, max-age=31536000, immutable
/files/*
  Cache-Control: public, max-age=3600
""")
    print("built")
