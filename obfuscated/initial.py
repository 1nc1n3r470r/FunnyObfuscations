"""
    This is my initial starting point

    I already published this once as a gist: https://gist.github.com/1nc1n3r470r/b93b501a6ee2e740032f1be1442ce988
"""
tmp = eval.__getattribute__("__self__")
in_script = tmp.getattr(tmp, "__dir__")()
print(-sorted(str(tmp.copyright)[:]).index(" "))
print(tmp.getattr(tmp,"__dict__")[tmp.getattr(tmp,"__dir__")()[-sorted(str(tmp.getattr(tmp,"copyright"))[:]).index(" ")]].__name__)
print(tmp.getattr(tmp,"__dict__")[tmp.getattr(tmp,"__dir__")()[len(tmp.getattr(tmp,"__dir__")()[-1])]].__reduce__()[-1].values().__iter__.__text_signature__)