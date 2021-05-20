import streamlit as st 
import pandas as pd 
import numpy as np 
#import matplotlib.pyplot as plt
from PIL import Image
import streamlit.components.v1 as components 
import sqlite3 

conn = sqlite3.connect('data.db')
c = conn.cursor()

# Security
#passlib,hashlib,bcrypt,scrypt
import hashlib
def make_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
	if make_hashes(password) == hashed_text:
		return hashed_text
	return False

#################################################
#############################################

def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')

def add_userdata(username,password):
	c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
	conn.commit()

def login_user(username,password):
	c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
	data = c.fetchall()
	return data

def view_all_users():
	c.execute('SELECT * FROM userstable')
	data = c.fetchall()
	return data
#def main():
st.markdown('<style>body{background-color: rgb(159, 177, 188);}</style>',unsafe_allow_html=True)
#st.markdown('<html><style>div{background-image:linear-gradient(to right,red,blue);}</style><html>',unsafe_allow_html=True)



st.markdown("""<style>.css-1aumxhk {
background-color:rgb(110, 136, 151);
background-image: none;
color: #ffffff
}</style>""", unsafe_allow_html=True)
#st.title("Record and Analyze Blast Operation Data")
menu = ["Home","Login","SignUp"]
choice = st.sidebar.selectbox("Menu",menu)

if choice == "Home":
    components.html("""
                    <style>
                    .city {
                    background-color: rgb(159, 177, 188);
                    color: white;
                    border: 1px solid black;
                    margin: 5px;
                    padding: 5px;
                    text-align: center;
                    font-size:35px !important;
                    font-family:"B mitra", serif;
                    }
                    </style>
                    <body>
                    <div class="city"><h2>واحد آموزش و نیروی انسانی</h2></div> 
                    """,width=750, height=200, scrolling=False)
                
    pic = Image.open('LOGO.jpg')
    st.image(pic,width=500)
    #pi = Image.open('p.jpg')
    #st.image(pi, use_column_width=True)

    st.markdown("""
    <style>
    .big-font {
        font-size:40px !important;font-family:"B mitra", serif; color: blue;text-align: center;
    }
    </style><p class="big-font">تنها امتیاز رقابتی سازمان ها در سده 21 بر خورداری از کارکنان فرهیخته و ارزش‌مند است و بهره برداری از این کارکنان بزرگ ترین چالشی است که مدیران در این سده با آن رو به رو هستند</p>
    """, unsafe_allow_html=True)

    st.markdown("""
    <style>
    .big-font {
        font-size:30px !important;font-family:"B mitra", serif;
    }
    </style><p class="big-font">"(مایکل ارمسترانگ)"</p>
    """, unsafe_allow_html=True)
elif choice == "Login":
    #st.subheader("Login Section")
    username = st.sidebar.text_input("User Name")
    password = st.sidebar.text_input("Password",type='password')
    if st.sidebar.checkbox("Login"):
        # if password == '12345':
        create_usertable()
        hashed_pswd = make_hashes(password)

        result = login_user(username,check_hashes(password,hashed_pswd))
        if result:
            #st.set_page_config(layout="wide")
            pages = ["RIASEC",'TDT Survey']
            page = st.sidebar.radio("Behin Rahbord Enfejar", options=pages)

            if page == "RIASEC":
                st.write('RIASEC')
            elif page == "TDT Survey":
                components.html("""
                <style>
                .big-font {
                    font-size:40px !important;font-family:"B mitra", serif;background-color:#6296D5;text-align:center;
                }
                </style> <h2 class="big-font">Decision Style</h2>
                """,height=80)
                components.html("""
                <style>
                .big-font {
                    font-size:40px !important;font-family:"B mitra", serif;background-color:#6296D5;text-align:center;
                }
                </style> <h2 class="big-font">Temperament Survey</h2>
                """, height=80)
                components.html("""
                <style>
                .big-font {
                    font-size:40px !important;font-family:"B mitra", serif;background-color:#6296D5;text-align:center;
                }
                </style> <h2 class="big-font">Thinkig Style</h2>
                """,height=80)
                
                components.html("""
                <style>
                .big-font {
                    font-size:20px !important;font-family:"B mitra", serif; color: black;text-align:right;
                }
                </style> <p class="big-font">در پاسخ به سؤالات گزینه‌ای را انتخاب کنید که ویژگی‌ها و شخصیت واقعی شما را توصیف کند و نه ویژگی‌هایی که می‌خواهید داشته باشید و یا دیگران از شما توقع دارند.
                    پاسخ درست یا غلط وجود ندارد.
                    صادقانه پاسخ دهید تا بتوانید به شخصیت واقعی خود پی ببرید</p>
                    """)
                o11 =['A-','AB-','A+','AB+','B-','O-','B+','O+']
                qq11=st.selectbox("گروه خونی شما چیست؟",o11)

                o1 = ["الف- پرپشت، کلفت، تیره و صاف","ب- پرپشت، کلفت، تیره و مجعد","ج- پرپشت، کلفت، لخت (کم پشت) و روشن","د. کم پشت، نرم و نازک و شکننده و چرب"]
                qq1=st.selectbox(" وضعیت موهای بدن اعم از سر و بدن به چه شکلی است؟",o1)

                o2 = ["الف- گندمگون سبزه", "ب- گلگون", "ج- سفیدی رو به مهتابی", "د-گندمون به سمت تیرگی و مات"]
                qq2=st.selectbox("رنگ پوست شما چه رنگی است؟",o2)

                o3 = ["الف- مشکی پر کلاغی", "ب- مشکی معمولی یا خرمایی پر رنگ", "ج- خرمایی روشن (رو به روشنی)","د- مشکی کدر"]
                qq3=st.selectbox("رنگ مو شما چه رنگی است؟",o3)


                o4= ["الف- قرمز تیره", "ب- قرمز روشن", "ج- کم رنگ رو به سفیدی","د- قهوه ای تیره"]
                qq4=st.selectbox("رنگ لب شما چه رنگی است؟",o4)

                o5 = ["الف- رگ، کاملاً  پیدا و برجسته", "ب- رگ، نیمه آشکار و با رطوبت", "ج- رگ، پنهان و برجستگی ندارد","د- رگ، برجسته نیست ولی دیده می شود و رنگ آن تیره است"]
                qq5=st.selectbox("وضعیت عروق شما چگونه است؟",o5)

                o6 = ["الف- مشکی یا میشی پر رنگ براق", "ب- مشکی معمولی", "ج- رنگ‌های روشن","د- مشکی و رنگ‌های تیره مات"]
                qq6=st.selectbox("رنگ مردمک چشم شما چه رنگی است؟",o6)

                o7 = ["الف- سفید و براق", "ب- رو به قرمزی و براق", "ج- لکه های قهوه ای در سفیدی چشم بدون براقی","د- رو به تیرگی و ماتی و کدری"]
                qq7=st.selectbox("ترکیب سفیدی چشم شما چه رنگی است؟",o7)

                o8 = ["الف- بلند", "ب- متوسط", "ج- کوتاه","د- خیلی کوتاه"]
                qq8=st.selectbox("ساختار اندازه بلندی پیشانی شما چگونه است؟",o8)

                o9 = ["الف- زیاد", "ب- متوسط", "ج- کم","د-خیلی کم"]
                qq9=st.selectbox("اگر تذکرات دیگران نباشد، اشتهای شما چه شکل است؟",o9)

                o10 = ["الف- مربع", "ب- مستطیلی و کشیده", "ج- مستطیلی عمود بر انگشتان","د- دایره‌ای"]
                qq10=st.selectbox("کف دستتان از نظر هندسی چه شکلی است؟",o10)
                col110, col120, col130,col140 = st.beta_columns(4)

                with col110:
                    st.markdown("""
                        <style>
                        .big-font {
                            font-size:30px !important;font-family:"B mitra", serif; color: blue;text-align:center;
                        }
                        </style> <h2 class="big-font">الف- مربع</h2>
                        """, unsafe_allow_html=True)
                    pic110 = Image.open('110.png')
                    st.image(pic110, use_column_width=True)

                with col120:
                    st.markdown("""
                        <style>
                        .big-font {
                            font-size:25px !important;font-family:"B mitra", serif; color:black; text-align:center;
                        }
                        </style> <h2 class="big-font">ب-مستطیلی و کشیده</h2>
                        """, unsafe_allow_html=True)
                    pic120 = Image.open('120.png')
                    st.image(pic120, use_column_width=True)

                with col130:
                    st.markdown("""
                        <style>
                        .big-font {
                            font-size:25px !important;font-family:"B mitra", serif; color:black; text-align:center;
                        }
                        </style> <h2 class="big-font">ج- مستطیلی عمود بر انگشتان</h2>
                        """, unsafe_allow_html=True)
                    pic130 = Image.open('130.png')
                    st.image(pic130, use_column_width=True)

                with col140:
                    st.markdown("""
                        <style>
                        .big-font {
                            font-size:25px !important;font-family:"B mitra", serif; color:black; text-align:center;
                        }
                        </style> <h2 class="big-font">د- دایره‌ای</h2>
                        """, unsafe_allow_html=True)
                    pic140 = Image.open('140.png')
                    st.image(pic140, use_column_width=True)
                
                o12 = ["الف-کلفت(بزرگ و آشکار)", "ب- متوسط(بزرگ و پنهان)", "ج- کوچک و آشکار","د- کوچک و پنهان"]
                qq12=st.selectbox("فرم لب شما چه شکل است؟",o12)
                col210, col220, col230,col240 = st.beta_columns(4)

                with col210:
                    st.markdown("""
                        <style>
                        .big-font {
                            font-size:30px !important;font-family:"B mitra", serif; color: blue;text-align:center;
                        }
                        </style> <h2 class="big-font">الف- کلفت(بزرگ و آشکار)</h2>
                        """, unsafe_allow_html=True)
                    pic210 = Image.open('210.png')
                    st.image(pic210, use_column_width=True)

                with col220:
                    st.markdown("""
                        <style>
                        .big-font {
                            font-size:25px !important;font-family:"B mitra", serif; color:black; text-align:center;
                        }
                        </style> <h2 class="big-font">ب- متوسط (بزرگ و پنهان)</h2>
                        """, unsafe_allow_html=True)
                    pic220 = Image.open('220.png')
                    st.image(pic220, use_column_width=True)

                with col230:
                    st.markdown("""
                        <style>
                        .big-font {
                            font-size:25px !important;font-family:"B mitra", serif; color:black; text-align:center;
                        }
                        </style> <h2 class="big-font">ج- کوچک و آشکار"</h2>
                        """, unsafe_allow_html=True)
                    pic230 = Image.open('230.png')
                    st.image(pic230, use_column_width=True)

                with col240:
                    st.markdown("""
                        <style>
                        .big-font {
                            font-size:25px !important;font-family:"B mitra", serif; color:black; text-align:center;
                        }
                        </style> <h2 class="big-font">د- کوچک و پنهان</h2>
                        """, unsafe_allow_html=True)
                    pic240 = Image.open('240.png')
                    st.image(pic240, use_column_width=True)



            #elif page == "آزمون شماره 2":

                components.html("""
                <style>
                .big-font {
                    font-size:50px !important;font-family:"B mitra", serif; color: blue;text-align:center;
                }
                </style> <h2 class="big-font">آزمون شماره 2</h2>
                """)

                options = ["خیلی زیاد", "زیاد", "متوسط", "کم","خیلی کم"]
                q1=st.selectbox(" من به زمان بندی در کارها اهمیت می دهم",options)
                q2=st.selectbox(" برای تصمیمات مهم اطلاعات کامل و صحیح را جمع آوری می کنم",options)
                q3=st.selectbox(" در مواقع رو به رو شدن با خطرات احتمالی و فشار زمانی موقعیت را به خوبی اداره می کنم",options)
                q4=st.selectbox("  نتایج و پیامدهای فعالیت هایم را مورد ارزیابی قرار می‌دهم",options)
                q5=st.selectbox("  داده های مورد نیاز فعالیت هایم را مورد ارزیابی قرار می‌دهم",options)
                q6=st.selectbox(" ایده های موجود را با روشی جدید و یا در قبال موقعیت های جدید به کار می‌گیرم",options)
                q7=st.selectbox(" نتایج و عملکرد نهائی کارها برایم اهمیت زیادی دارد",options)
                q8=st.selectbox(" در انجام کارها هم نتیجه و هم روش برایم اهمیت دارد",options)
                q9=st.selectbox(" غالباً در جستجو فرصت ها و زمینه های جدید انجام کار، ایجاد مدل‌های بدیع و روش های نو هستم",options)
                q10=st.selectbox("  برنامه های آموزشی باید بر مبنای اندازه گیری های دقیق، داده های صحیح، تجزیه و تحلیل کامل صورت گیرد",options)
                q11=st.selectbox("  مدیریت کارآمد باید همواره نظرات و پیشنهاد های کارکنان و پرسنل را مد نظر قرار دهد",options)
                q12=st.selectbox(" در دسترس بودن داده ها و اطلاعات برای پرسنل اهمیت بسیاری دارد",options)
                q13=st.selectbox(" مدیران باید همواره تغییرات را در محیط کار طراحی و تدوین کنند",options)
                q14=st.selectbox(" به نظر شما تحقیق به عنوان ابزار موثر ایجاد زمینه برای خلاقیت و نوآوری تا چه اندازه اهمیت دارد",options)
                q15=st.selectbox("  آیا به حمایت همکاران خود در کار اهمیت زیادی می دهید؟ ",options)
                q16=st.selectbox(" در محیط کاری، پاسخگوی نظرات همکاران، همترازان، رؤسا و ارباب رجوع به روش سازنده هستم",options)
                q17=st.selectbox(" در کارهای تیمی و مشارکتها اطلاعات ضروری را به طور مرتب به همه ارائه می کنم",options)
                q18=st.selectbox(" حقایق و مسائل کاری را به صورت مکتوب و سازماندهی شده ارائه می کنم",options)
                q19=st.selectbox(" جلسات را به روشی که امکان رسیدن به نتایج کاملا مشخص و روشن باشد، سازماندهی می کنم",options)
                q20=st.selectbox(" از نقطه نظراتم در مقابل دیگران به خوبی دفاع می کنم",options)
                q21=st.selectbox(" گزارشات شفاهی را به صورت صریح و روشن به افراد ارائه می کنم",options)
                q22=st.selectbox(" درصورت لزوم تصمیمات سخت می گیرم",options)
                q23=st.selectbox(" به هنگام عدم وجود اطلاعات (با اطلاعات ناقص) بهترین تصمیم ممکن را می گیرم",options)
                q24=st.selectbox(" در جلسات و مشورتهای کاری با مطرح کردن سوالات مختلف باعث می‌شوم که کارکنان ابعاد دیگر مسائل را ببیند",options)
                q25=st.selectbox("  تغییرات لازم را بر اساس اولویت به خوبی انجام می‌دهم",options)
                q26=st.selectbox("  در مواجه با موانع قابلیت تصمیم گیری منطقی را دارم",options)
                q27=st.selectbox("  همیشه به دنبال کشف زمینه های مشترک کاری در سازمان هستم",options)
                q28=st.selectbox(" بدون توجه به محدوده کاری خود به دنبال یافتن زمینه های مشترک کاری باذی نفعان هستم",options)
                q29=st.selectbox(" هنگام کار با گروهی که به تضاد و کشمکش می رسد با یافتن نظرات مشترک به انجام امور کمک می کنم",options)
                q30=st.selectbox(" در نوشتن و ارتباطات شفاهی و همچنین گوش دادن به آسودگی عمل می کنم",options)
                q31=st.selectbox(" من اقدام به هدفگزاری نموده و برای هر چیزی یک چشم انداز بلند مدت تعیین می کنم، تا همین امور را انجام دهند",options)
                q32=st.selectbox(" در برابر رخدادهای تصادفی تا سر حد رها کردن برنامه جاری خود، حساسیت و عکس العمل نشان می دهیم",options)
                q33=st.selectbox(" خطرات و شکست های احتمالی را مانعی برای طرح جدید و یا نظرات جدید نمی دانم",options)


                components.html("""
                <style>
                .big-font {
                    font-size:50px !important;font-family:"B mitra", serif; color: blue;text-align:center;
                }
                </style> <h2 class="big-font">آزمون شماره 3</h2>
                """)

                options2 = ['کاملاً','بسیار زیاد','زیاد','تاحدودی','کم','بسیار کم','اصلاً']

                p1=st.selectbox(" هنگام رويارو شدن با يك مساله ،انديشه ها و روش هاي خودم را براي حل آن به كار مي برم",options2)
                p2=st.selectbox(" دوست دارم با افكارم بازي بكنم و ببينم آنها به چه چيزي منتهي مي شوند",options2)
                p3=st.selectbox(" مسائلي را دوست دارم که در آنها بتوانم راه حل هاي شخصي خودم را امتحان کنم",options2)
                p4=st.selectbox(" دوست دارم با افكار خودم ، كار را آغاز كنم",options2)
                p5=st.selectbox(" از موقعيت هايي كه فرصت استفاده از افكار و روش هاي خودم را دارم ، لذت مي برم",options2)
                p6=st.selectbox(" دوست دارم چگونگی حل یک مسئله بدنبال قوانين مشخص را بفهمم",options2)
                p7=st.selectbox(" دقت مي کنم که روش مناسبي را براي حل هر مسئله اي به کار ببرم",options2)
                p8=st.selectbox(" از کار کردن بر روي مسائلي که دستورالعمل مشخصي دارد، لذت مي برم",options2)
                p9=st.selectbox(" طرح هايي را دوست دارم كه ساختار روشني داشته و داراي برنامه و هدف مشخصي هستند",options2)
                p10=st.selectbox(" براي حل مشكل يا انجام دادن كار ، مايلم از دستورالعمل های مشخصي پيروي کنم",options2)
                p11=st.selectbox(" موقعيت هايي را دوست دارم که بتوانم روش هاي متفاوتِ انجام كارها را مقايسه و ارزیابی كنم",options2)
                p12=st.selectbox(" دوست دارم که نظرات متضاد و ديدگاه هاي متناقض را بررسي و ارزيابي کنم",options2)
                p13=st.selectbox(" طرح هايي را دوست دارم که بتوانم نظرات و ديدگاه هاي مختلف را مورد بررسي و ارزيابي قرار دهم",options2)
                p14=st.selectbox(" تکليف ها يا مسئله هايي را ترجيح مي دهم که بتوانم طرح ها يا روش های مورد استفادۀ ديگران را مورد ارزیابی قرار دهم",options2)
                p15=st.selectbox(" از كارهايي كه مستلزم تحليل، ارزيابي يا مقايسه اند ، لذت می برم ",options2)
########################################################
                def local_css(file_name):
                    with open(file_name) as f:
                        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

                def remote_css(url):
                    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)    

                def icon(icon_name):
                    st.markdown(f'<i class="material-icons">{icon_name}</i>', unsafe_allow_html=True)

                local_css("style.css")
                remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')

                icon("pageview")
                #selected = st.text_input("", "Search...")
                if st.button("مشاهده نتیجه"):

##########################################################

                #if st.button("مشاهده نتیجه"):
                        # model 1(all)
                    datad = []
                    datad.append([q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20,q21,q22,q23,q24,q25,q26,q27,q28,q29,q30,q31,q32,q33])
                    df = pd.DataFrame(datad,columns=('q1','q2','q3','q4','q5','q6','q7','q8','q9','q10','q11','q12','q13','q14','q15','q16','q17','q18','q19','q20','q21','q22','q23','q24','q25','q26','q27','q28','q29','q30','q31','q32','q33'))
                    df = df.replace(['خیلی زیاد'],'5')
                    df = df.replace(['زیاد'],'4')
                    df = df.replace(['متوسط'],'3')
                    df = df.replace(['کم'],'2')
                    df = df.replace(['خیلی کم'],'1')
                    df = df.astype(int)
                    #model 2 ( 1/2)
                    dq12 = []
                    dq12.append([q1,q2])
                    dfq12 = pd.DataFrame(dq12, columns= ('q1','q2'))
                    dfq12 = dfq12.replace(['خیلی زیاد'],'1')
                    dfq12 = dfq12.replace(['زیاد'],'2')
                    dfq12 = dfq12.replace(['متوسط'],'3')
                    dfq12 = dfq12.replace(['کم'],'4')
                    dfq12 = dfq12.replace(['خیلی کم'],'5')
                    dfq12 = dfq12.astype(int)
                    #model 3 (red 16/7/17)
                    dm3 = []
                    dm3.append([q16,q7,q17])
                    dfm3 = pd.DataFrame(dm3, columns= ('q16','q7','q17'))
                    dfm3 = dfm3.replace(['خیلی زیاد'],'4')
                    dfm3 = dfm3.replace(['زیاد'],'5')
                    dfm3 = dfm3.replace(['متوسط'],'3')
                    dfm3 = dfm3.replace(['کم'],'2')
                    dfm3 = dfm3.replace(['خیلی کم'],'1')
                    dfm3 = dfm3.astype(int)
                    #model 4 (blue 17/5/6)
                    dm4 = []
                    dm4.append([q17,q5,q6])
                    dfm4 = pd.DataFrame(dm4, columns= ('q17','q5','q6'))
                    dfm4 = dfm4.replace(['خیلی زیاد'],'3')
                    dfm4 = dfm4.replace(['زیاد'],'4')
                    dfm4 = dfm4.replace(['متوسط'],'5')
                    dfm4 = dfm4.replace(['کم'],'2')
                    dfm4 = dfm4.replace(['خیلی کم'],'1')
                    dfm4 = dfm4.astype(int)
                    #model 5 (23)
                    dm5 = []
                    dm5.append([q23])
                    dfm5 = pd.DataFrame(dm5,columns = ['q23'])
                    dfm5 = dfm5.replace(['خیلی زیاد'],'3')
                    dfm5 = dfm5.replace(['زیاد'],'5')
                    dfm5 = dfm5.replace(['متوسط'],'4')
                    dfm5 = dfm5.replace(['کم'],'2')
                    dfm5 = dfm5.replace(['خیلی کم'],'1')
                    dfm5 = dfm5.astype(int)
                    df['انعطاف پذیر'] = (dfm3['q16'] + dfm4['q17'] +dfm5['q23']+df['q24']+df['q28']+df['q29']+df['q1']+df['q8'])
                    df['فراگیر'] = (dfq12['q1'] + df['q24'] +df['q10']+df['q11']+df['q2']+df['q3']+df['q5']+df['q16']+df['q17']+df['q27']+df['q31']+df['q12']+df['q14'])
                    df['قاطع'] = (df['q4'] + dfm3['q7'] +df['q15']+df['q16']+df['q1']+dfq12['q2']+df['q23']+df['q22']+df['q13'])
                    df['سلسله مراتبی'] = (df['q32'] + dfm4['q5'] +dfm3['q17']+dfm4['q6']+df['q20']+df['q16']+df['q7']+df['q8']+df['q30']+df['q31']+df['q12'])

                    df['Total'] =  df['انعطاف پذیر'] + df['فراگیر'] + df['قاطع'] + df['سلسله مراتبی']
                    datat = []
                    datat.append([p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15])

                    df2 = pd.DataFrame(datat,columns =('p1','p2','p3','p4','p5','p6','p7','p8','p9','p10','p11','p12','p13','p14','p15'))
                    df2 = df2.replace(['کاملاً'],'7')
                    df2 = df2.replace(['بسیار زیاد'],'6')
                    df2 = df2.replace(['زیاد'],'5')
                    df2 = df2.replace(['تاحدودی'],'4')
                    df2 = df2.replace(['کم'],'3')
                    df2 = df2.replace(['بسیار کم'],'2')
                    df2 = df2.replace(['اصلاً'],'1')
                    df2 = df2.astype(int)

                    df2['قانون گذار'] = (df2['p1'] + df2['p2'] + df2['p3'] + df2['p4'] + df2['p5'])
                    df2['اجرایی محور'] = (df2['p6'] + df2['p7'] + df2['p8'] + df2['p9'] + df2['p10'])
                    df2['قضاوت گر'] = (df2['p11'] + df2['p12'] + df2['p13'] + df2['p14'] + df2['p15'])
                    df2new = pd.DataFrame(df2, columns = ['قانون گذار','اجرایی محور','قضاوت گر'])
                    #st.write(df2new)
                    #df2['a'] = (df2['p1'] + df2['p2'] + df2['p3'] + df2['p4'] + df2['p5'])
                    #df2['b'] = (df2['p6'] + df2['p7'] + df2['p8'] + df2['p9'] + df2['p10'])
                    #df2['c'] = (df2['p11'] + df2['p12'] + df2['p13'] + df2['p14'] + df2['p15'])
                    #df2new = pd.DataFrame(df2, columns = ['c','b','a'])
                    #st.write(df2new)
                    if (df2new.at[0,'قانون گذار'] > df2new.at[0,'اجرایی محور']) and (df2new.at[0,'قانون گذار'] > df2new.at[0,'قضاوت گر']):
                        components.html("""
                            <style>
                            .big-font {
                                font-size:35px !important;font-family:"B mitra", serif; color: black;text-align:center;
                            }
                            </style> <h2 class="big-font">:سبک تفکر شما</h2>
                            """)
                        pic001 = Image.open('LOW.jpg')
                        st.image(pic001,use_column_width=True)
                        components.html("""
                        <style>
                        .big-font {
                            font-size:25px !important;font-family:"B mitra", serif; color: black;text-align:right;
                        }
                        </style> <p class="big-font">دوست دارند کارها و روش‌های انجام آنها را خود خلق کنند. از اﻧﺠﺎم ﮐﺎرﻫﺎﯾﯽ ﮐﻪ ﻧﯿﺎز ﺑﻪ ﺧﻼﻗﯿﺖ و ﻃﺮاﺣﯽ دارد، ﻟﺬت ﻣﯽﺑﺮد و ﮐﺎرﻫﺎ را ﺑﻪ روش ﺧﻮد اﻧﺠﺎم ﻣﯽدﻫﺪ.</p>
                        """)
                        
                    elif (df2new.at[0,'قانون گذار'] < df2new.at[0,'اجرایی محور']) and (df2new.at[0,'قضاوت گر'] < df2new.at[0,'اجرایی محور']):
                        components.html("""
                            <style>
                            .big-font {
                                font-size:35px !important;font-family:"B mitra", serif; color: black;text-align:center;
                            }
                            </style> <h2 class="big-font">:سبک تفکر شما</h2>
                            """)
                        pic002 = Image.open('EXE.jpg')
                        st.image(pic002,use_column_width=True)
                        components.html("""
                        <style>
                        .big-font {
                            font-size:25px !important;font-family:"B mitra", serif; color: black;text-align:right;
                        }
                        </style> <p class="big-font">به مشاغلی گرایش دارند که همراه با راهنمایی و دستورالعمل باشد و در انجام کارها هیچ خلاقیتی از خود نشان نمی‌دهند
                        ﺑﻪ ﭘﯿﺮوی از دﺳﺘﻮرات ﺗﻤﺎﯾﻞ دارد و ﺑﯿﺸﺘﺮ ﺑﻪ ﮐﺎرﻫﺎﯾﯽ علاقه‌مند اﺳﺖ ﮐﻪ ﺑﺎ آﻣﻮزشﻫﺎی ﺻﺮﯾﺢ و روﺷﻦ ﻫﻤﺮاه ﺑﺎﺷﺪ.</p>
                        """)    

                    else :
                        components.html("""
                            <style>
                            .big-font {
                                font-size:35px !important;font-family:"B mitra", serif; color: black;text-align:center;
                            }
                            </style> <h2 class="big-font">:سبک تفکر شما</h2>
                            """)
                        pic003 = Image.open('JUD.jpg')
                        st.image(pic003,use_column_width=True)
                        components.html("""
                        <style>
                        .big-font {
                            font-size:25px !important;font-family:"B mitra", serif; color: black;text-align:right;
                        }
                        </style> <p class="big-font">دوست دارند نقش‌ها را ارزیابی کنند، درباره چیزها داوری کنند 
                        و ﺑﯿﺸﺘﺮ ﺗﻮﺟﻪ ﺧﻮد را ﺑﺮ ﻗﻀﺎوت و ارزﯾﺎﺑﯽ اﻓﺮاد و ﮐﺎرﻫﺎ ﻣﺘﻤﺮﮐﺰ ﻣﯽکنند</p>
                        """)
                    components.html("""
                            <style>
                            .big-font {
                                font-size:35px !important;font-family:"B mitra", serif; color: black;text-align:center;
                            }
                            </style> <h2 class="big-font">:سبک تصمیم‌گیری شما</h2>
                            """)    
                    if df.at[0,'سلسله مراتبی'] > 45:
                        
                        pic003 = Image.open('JUD.jpg')
                        pic3 = Image.open('سلسه مراتبی-01-01.jpg')
                        st.image(pic3, use_column_width=True)
                    if df.at[0,'فراگیر'] > 45:
                        pic4 = Image.open('فراگیر-01.jpg')
                        st.image(pic4, use_column_width=True)
                    if df.at[0,'قاطع'] > 35:
                        pic5 = Image.open('قاطع-01.jpg')
                        st.image(pic5, use_column_width=True)
                    if df.at[0,'انعطاف پذیر'] > 30:
                        pic6 = Image.open('انعطاف پذیر-01.jpg')
                        st.image(pic6, use_column_width=True)
                ######################################################################################
                    dqq12 = []
                    dqq12.append([qq2,qq3,qq4,qq5,qq6,qq7,qq8,qq9,qq10,qq12])

                    #dfqq12 = pd.DataFrame(dqq12, columns= ('qq2','qq3','qq4','qq5','qq6','qq7','qq8','qq9','qq10','qq12'))
                    dfqq12 = pd.DataFrame({"caca":[qq2,qq3,qq4,qq5,qq6,qq7,qq8,qq9,qq10,qq12]})

                    dfqq12 = dfqq12.replace(["الف- گندمگون سبزه","الف- پرپشت، کلفت، تیره و صاف","الف- مشکی پر کلاغی","الف- قرمز تیره","الف- رگ، کاملاً  پیدا و برجسته","الف- مشکی یا میشی پر رنگ براق","الف- سفید و براق","الف- بلند","الف- زیاد","الف- مربع","الف-کلفت(بزرگ و آشکار)",],'A')
                    dfqq12 = dfqq12.replace(["ب- متوسط",'ب- پرپشت، کلفت، تیره و مجعد',"ب- گلگون","ب- مشکی معمولی یا خرمایی پر رنگ","ب- قرمز روشن","ب- رگ، نیمه آشکار و با رطوبت","ب- مشکی معمولی", "ب- رو به قرمزی و براق","ب- متوسط","ب- مستطیلی و کشیده","ب- متوسط(بزرگ و پنهان)",],'B')
                    dfqq12 = dfqq12.replace(["ج- کم رنگ رو به سفیدی","ج- پرپشت، کلفت، لخت (کم پشت) و روشن","ج- سفیدی رو به مهتابی","ج- خرمایی روشن (رو به روشنی)","ج- رگ، پنهان و برجستگی ندارد", "ج- رنگ‌های روشن","ج- لکه های قهوه ای در سفیدی چشم بدون براقی","ج- کوتاه","ج- کم","ج- مستطیلی عمود بر انگشتان","ج- کوچک و آشکار"],'C')
                    dfqq12 = dfqq12.replace(["د. کم پشت، نرم و نازک و شکننده و چرب","د- مشکی کدر","د- قهوه ای تیره","د- مشکی و رنگ‌های تیره مات","د- رگ، برجسته نیست ولی دیده می شود و رنگ آن تیره است","د- رو به تیرگی و ماتی و کدری","د- خیلی کوتاه","د- دایره‌ای","د-خیلی کم","د- کوچک و پنهان"],'D')
                    
                    #DD.count(level='0')
                    #st.write(dfqq12['caca'].value_counts())
                    #st.write(dfqq12['caca'].value_counts().idxmax())
                    mezaj = dfqq12['caca'].value_counts().idxmax()
                    if mezaj == 'A':
                        components.html("""
                            <style>
                            .big-font {
                                font-size:35px !important;font-family:"B mitra", serif; color:black;text-align:center;
                            }
                            </style> <h2 class="big-font">:طبع و مزاج شما</h2>
                            """)
                        pic33 = Image.open('q1.jpg')
                        st.image(pic33)
                    if mezaj == 'B':
                        components.html("""
                            <style>
                            .big-font {
                                font-size:35px !important;font-family:"B mitra", serif; color: black;text-align:center;
                            }
                            </style> <h2 class="big-font">:طبع و مزاج شما</h2>
                            """)
                        pic44 = Image.open('q4.jpg')
                        st.image(pic44)
                    if mezaj == 'C':
                        components.html("""
                            <style>
                            .big-font {
                                font-size:35px !important;font-family:"B mitra", serif; color: black;text-align:center;
                            }
                            </style> <h2 class="big-font">:طبع و مزاج شما</h2>
                            """)
                        pic55 = Image.open('q3.jpg')
                        st.image(pic55)
                    if mezaj == 'D':
                        components.html("""
                            <style>
                            .big-font {
                                font-size:35px !important;font-family:"B mitra", serif; color: black;text-align:center;
                            }
                            </style> <h2 class="big-font">:طبع و مزاج شما</h2>
                            """)
                        pic66 = Image.open('q2.jpg')
                        st.image(pic66)
elif choice == "SignUp":
    st.subheader("Create New Account")
    new_user = st.text_input("Username")
    new_password = st.text_input("Password",type='password')

    if st.button("Signup"):
        create_usertable()
        add_userdata(new_user,make_hashes(new_password))
        st.success("You have successfully created a valid Account")
        st.info("Go to Login Menu to login")