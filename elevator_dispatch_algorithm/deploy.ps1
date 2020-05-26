
git clone https://github.com/117503445/elevator_dispatch.git
cd elevator_dispatch
docker build -t 117503445/elevator_dispatch .
docker run --name elevator_dispatch -p 8006:80 -d --restart always 117503445/elevator_dispatch
docker rm elevator_dispatch -f