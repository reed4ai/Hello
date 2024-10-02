def database_connect(username, password):
    pass


def connect_to_database():
    # 不安全的：hard code編碼帳號密碼在程式碼中
    username = "admin"
    password = "password"
    # 假設有一個資料庫連線的函數
    database_connect(username, password)

    print("Connected to database using username and password", username, password)


def query_user_data(user_id):
    pass


def main():
    connect_to_database
    query_user_data(1)
    print("Done!")


if __name__ == "__main__":
    main()
