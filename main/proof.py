import hashlib

seed = 'yrw6T6596icnddcUTWaxBF4UpiRcX0XF'
sha = hashlib.sha512


def is_good(test):
    hashed = sha(test.encode('utf-8')).hexdigest()
    if hashed[:4] == "0000":
        return True
    else:
        return False


def do_proof(previous_step):
    found = False
    step = int(previous_step[len(seed):]) + 1
    while found is False:
        test_proof = seed + str(step)
        found = is_good(test_proof)
        step = step + 1
    return test_proof
