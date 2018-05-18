
def validate_on_save(cls):
    base_save = cls.save

    def save(slf, *args, **kwargs):
        slf.full_clean()
        base_save(slf, *args, **kwargs)
    cls.save = save

    return cls
