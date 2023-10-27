import hashlib

url_mapping = {}

def shorten_url(long_url):
        #generate a unique short url from the long url
        short_url = hashlib.md5(long_url.encode()).hexdigest()[:8]
        url_mapping[short_url]=long_url
        return short_url

def expand_url(short_url):
        #retrive the long url from the short url
        long_url = url_mapping.get(short_url)
        return long_url
  
def main():
        while True:
            print("\nURL shortener")
            print("1. shorten URL")
            print("2. expand URL")
            print("3.exit")
            choice = input("select an option: ")

            if choice == '1':
                long_url = input("enter the long URL to shorten: ")
                short_url = shorten_url(long_url)
                print(f"shortened URL:  {short_url}")

            elif choice == '2':
                short_url = input("enter the short URL to expand: ")
                long_url = expand_url(short_url)
                if long_url:
                    print(f"expanded URL: {long_url}")
                else:
                    print("short URL not found.")

            elif choice == '3':
                break
            
            else:
                 print("invalid choice. please select a value option.")

if __name__ == "__main__":
    main()
