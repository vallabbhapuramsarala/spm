from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
def token(rollno,seconds):
    s=Serializer('sarru2002',seconds)
    return s.dumps({'user':rollno}).decode('utf-8')
