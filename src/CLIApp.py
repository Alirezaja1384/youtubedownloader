# pip install pytube
from pytube import YouTube, exceptions


def download_video(url):
    x = YouTube(url)
    print(x.streams)
    # x.streams.last().download()


def main():
    a = input("Give me your youtube link: ")
    try:
        download_video(a)
    except exceptions.RegexMatchError:
        print("The input is not a youtube video link !")
    except:
        raise


if __name__ == "__main__":
    main()
