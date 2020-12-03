def finding_valid_passwords_old_policy(passwords):
    num_valid = 0
    for password in passwords:
        policy = password.split(":")[0]
        cur_pass = password.split(":")[1].strip()
        let = policy[-1]
        min_policy, max_policy = list(map(int, policy.split()[0].split("-")))
        let_count = cur_pass.count(let)
        if let_count >= min_policy and let_count <= max_policy:
            num_valid += 1
    return num_valid


def finding_valid_passwords_new_policy(passwords):
    num_valid = 0
    for password in passwords:
        policy = password.split(":")[0]
        cur_pass = password.split(":")[1].strip()
        let = policy[-1]
        pos_one, pos_two = list(map(int, policy.split()[0].split("-")))
        # since there is no concept of zero in the password policy, have to do a
        # -1 and shift everything to the left
        if (cur_pass[pos_one - 1] == let) ^ (cur_pass[pos_two - 1] == let):
            num_valid += 1
    return num_valid


if __name__ == "__main__":
    with open("input.txt", "r") as fh:
        passwords = fh.read().split("\n")

    print(finding_valid_passwords_old_policy(passwords))
    print(finding_valid_passwords_new_policy(passwords))
