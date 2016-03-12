def atomic( token ):
    try:
        return int(token)
    except ValueError:
        try return float(token)
        except ValueError:
            return str(token)
