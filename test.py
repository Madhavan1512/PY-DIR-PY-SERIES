def remote_control_next():
    yield "cnn"
    yield "espn"
itr = remote_control_next()
print(itr)
print(next(itr))
print(next(itr))


