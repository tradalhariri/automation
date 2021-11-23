import re
# (\(?\d{3}\)?)?-?
email_pattern = r"[\w\.\-]+@[\w\.-]+"
# phone_pattern = r"((\(\d{3}\))|(\d{3}-))\d{3}-\d{4}"
# phone_pattern = r"([+]?[(]?[0-9]{1,4}[)]?)([-|.]?[0-9]{1,4})([-|.]?[0-9]{1,4})([-|.]?([0-9]{1,4})?)([x]?([0-9]{1,7})?)"
# phone_pattern = r"[(\(\d{3}\))|\d{3}]-?\d{3}-\d{4}"
# phone_pattern = r"(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{3}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{3})"
phone_pattern = r"(\d{3}-\d{3}-\d{4}|\(\d{3}\)\s?\d{3}-\d{4}|\d{3}-\d{4})"




def from_file_to_str(path):
    file_as_str = ""
    with open(path, 'r') as f:
        file_as_str = f.read()
    return file_as_str

def get_emailes(content):
    emailes = re.findall(email_pattern, content)
    emailes = list(set(emailes))
    emailes.sort()

    return emailes

def get_phones(content):
    phones = re.findall(phone_pattern, content)
    phones = list(set(phones))
    phones.sort()
    return phones

def create_file(path,content):
    with open(path, 'w') as f:
        f.write('\n'.join(content))


if __name__ == '__main__':
    print(get_emailes(from_file_to_str("automation/assets/potential-contacts.txt")))
    print(get_phones(from_file_to_str("automation/assets/potential-contacts.txt")))
    print(len(get_emailes(from_file_to_str("automation/assets/potential-contacts.txt"))))
    print(len(get_phones(from_file_to_str("automation/assets/potential-contacts.txt"))))
    create_file("automation/assets/phone_numbers.txt",get_phones(from_file_to_str("automation/assets/potential-contacts.txt")))
    create_file("automation/assets/emails.txt",get_emailes(from_file_to_str("automation/assets/potential-contacts.txt")))



