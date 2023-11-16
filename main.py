import os
import requests
import zipfile
import datetime

def download_newspapers(daynumber, newspapers = ["NY_NYT"], zip=True, zipfile_name = "newspapers.zip", keepfiles=True, showprogress=True):
    if zip and os.path.exists(zipfile_name):
        os.remove(zipfile_name)

    for n in newspapers:
        
        # PDF URL
        # https://cdn.freedomforum.org/dfp/pdf15/AUT_SN.pdf
        
        url = f"https://cdn.freedomforum.org/dfp/pdf{daynumber}/{n}.pdf"
        #url = f"https://cdn.freedomforum.org/dfp/jpg{daynumber}/lg/{n}.jpg"
        filename = f"{n}.pdf"

        if showprogress:
            print(f"Downloading {url} to {filename}")
        response = requests.get(url)
        with open(filename, 'wb') as f:
            f.write(response.content)
        
        if zip:
            with zipfile.ZipFile(zipfile_name, "a") as zipf:
                zipf.write(filename)

        if not keepfiles:
            os.remove(filename)

if __name__ == "__main__":
    newspapers = ["CA_LAT",
                "DC_WP",
                "IL_CT",
                "JPN_JT",
                "MA_BG",
                "NY_DN",
                "NY_NYT",
                "UAE_GN",
                "UK_MAIL",
                "WSJ",]
    daynumber = datetime.date.today().day
    download_newspapers(daynumber, newspapers=newspapers, keepfiles=True)
