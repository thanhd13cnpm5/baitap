from flask import Flask, jsonify, request
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))


@app.route("/getLogLine", methods=["GET","POST"])
def getLogLine():
    # mở file ở chế độ đọc
    f = open("linux.log", "r")
    dem = 0
    # lấy dòng mà người dùng nhập vào
    line = request.json["line"]
    while True:
        # đọc từng dòng tròng vòng lặp và tăng biến đếm sau mỗi lần đọc
        txt = f.readline().rstrip("\n")
        dem += 1
        # kiểm tra dòng mà người dùng nhập vào khớp với biến đếm
        if dem == line:
            # tìm vị trí các ký tự
            find1 = txt.find("[")
            find2 = txt.find("]")
            find3 = txt.find(";")
            if find1 == -1:# nếu không tồn tại find1
                time = txt[0:15]
                host = txt[16:21]
                appname = txt[txt.find(host) + len(host):txt.find(": ")]
                message = txt[txt.find(appname) + len(appname)+1:]
                return jsonify({
                    "time": time,
                    "host": host,
                    "appname": appname,
                    "message": message
                })
            else: #nếu tồn tại find1
                time = txt[0:15]
                host = txt[16:21]
                appname = txt[txt.find(host)+len(host)+1:find1]
                appid = txt[txt.find(appname)+len(appname)+1:find2]
            if find3 == -1:# nếu không tồn tại
                message = txt[txt.find(appid)+len(appid)+2:]
                return jsonify({"time": time,
                                "host": host,
                                "appname": appname,
                                "appid": appid,
                                "message": message})
            else:#nếu tồn tại
                message = txt[txt.find(appid)+len(appid)+2:find3]
                find4 = txt.find("logname")
                if find4 != -1:# nếu không tồn tại
                    logname = txt[txt.find("logname=") + len("logname="):txt.find("uid")]
                    uid = txt[txt.find("uid=") + len("uid="):txt.find("euid")]
                    euid = txt[txt.find("euid=") + len("euid="):txt.find("tty")]
                    tty = txt[txt.find("tty=") + len("tty="):txt.find("ruser")]
                    ruser = txt[txt.find("ruser=") + len("ruser="):txt.find("rhost")]
                    rhost = txt[txt.find("rhost=") + len("rhost="):]
                    return jsonify({"time": time,
                                    "host": host,
                                    "appname": appname,
                                    "appid": appid,
                                    "message": message,
                                    "logname": logname,
                                    "uid": uid,
                                    "euid": euid,
                                    "tty": tty,
                                    "ruser": ruser,
                                    "rhost": rhost})
                else:#nếu tồn tại
                    return jsonify({"time": time,
                                "host": host,
                                "appname": appname,
                                "appid": appid,
                                "message": message})
            break





if __name__=="__main__":
    app.run(debug=True)