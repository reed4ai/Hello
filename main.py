from db import connect_to_database, query_user_data


def main():
    connect_to_database
    query_user_data(1)
    print("Done!")


if __name__ == "__main__":
    main()
