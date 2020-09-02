import requests
import concurrent.futures
import time


def download(url):
    print("Download Started")
    name = url.split("/")[9].split(".")[0]
    data = requests.get(url).content
    with open(f"{name}.png", "wb") as img:
        img.write(data)
    print("Download Finished")


urls = ["https://cdn.pixabay.com/photo/2020/08/22/05/58/woman-5507606_960_720.jpg",
        "https://cdn.pixabay.com/photo/2020/08/23/04/16/mont-st-michel-5509839__340.jpg",
        "https://cdn.pixabay.com/photo/2020/08/23/22/00/cologne-cathedral-5512117__340.jpg",
        "https://cdn.pixabay.com/photo/2020/08/23/17/33/lightning-5511473__340.jpg",
        "https://cdn.pixabay.com/photo/2020/04/18/18/12/portrait-5060365__340.jpg",
        "https://cdn.pixabay.com/photo/2020/07/07/13/52/woman-5380651__340.jpg"
        ]
t1 = time.time()
with concurrent.futures.ThreadPoolExecutor() as exc:
    exc.map(download, urls)
print(f"Download Finished in {time.time() - t1}")
