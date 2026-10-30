from langchain_community.document_loaders import WebBaseLoader


url="https://www.flipkart.com/samsung-galaxy-book4-metal-intel-core-i3-13th-gen-1315u-8-gb-512-gb-ssd-windows-11-home-np750xgj-lg9in-thin-light-laptop/p/itmc29d559898e6f?pid=COMH4Y6KKRC9YSWE&lid=LSTCOMH4Y6KKRC9YSWERDUMZD&marketplace=FLIPKART&store=6bo%2Fb5g&srno=b_1_1&otracker=browse&fm=organic&iid=8bfa6844-b848-4161-b67e-ad1f2623297b.COMH4Y6KKRC9YSWE.SEARCH&ppt=hp&ppn=homepage&ssid=r67w2dlse80000001793339379204&ov_redirect=true"

loader=WebBaseLoader(url)
docs=loader.load()

print(docs[0].page_content)