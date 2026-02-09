def comma_and(string_list):
    if not string_list:
        return ""
    elif len(string_list)==1:
        return string_list[0]
    elif len(string_list)==2:
        return f"{string_list[0]} and {string_list[1]}"
    else:
        return f"{', '.join(string_list[:-1])} and {string_list[-1]}"

def main():
    items=[]
    while True:
        item=input("Enter a string (or press Enter to stop): ")
        if item=="":
            break
        items.append(item)

    result=comma_and(items)
    print(result)

if __name__ == "__main__":
    main()