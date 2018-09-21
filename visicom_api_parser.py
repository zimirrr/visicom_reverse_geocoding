def parse_featureCollection(features):
    """ 
    returns array of dicts
    every obj hast keys 'id', 'category'
    other keys depends on category
    """
    parsed_features = []
    for feature in features:
        category = feature['properties']['categories']
        if category == 'adr_address':
            parsed_features.append(parse_adr(feature))
        elif category == 'adr_street':
            parsed_features.append(parse_str(feature))
        elif category == 'adm_settlement':
            parsed_features.append(parse_stl(feature))
        elif category == 'adm_level1':
            parsed_features.append(parse_adm1(feature))
        elif category == 'adm_level2':
            parsed_features.append(parse_adm2(feature))
        elif category == 'adm_district':
            parsed_features.append(parse_dst(feature))
        elif category == 'adm_country':
            parsed_features.append(parse_cnt(feature))

    return parsed_features

# def parse_feature(feature):
#     """ 
#     returns dict
#     every obj hast keys 'id', 'category'
#     other keys depends on category
#     """

#     category = feature['properties']['categories']
#     if category == 'adr_address':
#         parsed_feature = parse_adr(feature)
#     elif category == 'adr_street':
#         parsed_feature = parse_str(feature)
#     elif category == 'adm_settlement':
#         parsed_feature = parse_stl(feature)
#     elif category == 'adm_level1':
#         parsed_feature = parse_adm1(feature)
#     elif category == 'adm_level2':
#         parsed_feature = parse_adm2(feature)
#     elif category == 'adm_district':
#         parsed_feature = parse_dst(feature)
#     elif category == 'adm_country':
#         parsed_feature = parse_cnt(feature)

#     return parsed_feature

def parse_adr(feature):
    """
    returns dict
    'id', 'category' - required keys
    'dist_meters' - distance from point in search
    """
    res = {
        'id' : feature['id'],
        'category' : 'adr_address',
        'adr_name' : feature['properties']['name'],
        'str_name' : feature['properties']['street'],
        'str_type' : feature['properties']['street_type'],
        'stl_name' : feature['properties']['settlement'],
        'stl_type' : feature['properties']['settlement_type'],
        'stl_id' : feature['properties']['settlement_id'],
        'dist_meters' : feature['properties']['dist_meters']
    }

    try:
        res['geometry'] = feature['geometry']
    except:
        pass
    return res

def parse_str(feature):
    """
    returns dict
    'id', 'category' - required keys
    'dist_meters' - distance from point in search
    """
    res = {
        'id' : feature['id'],
        'category' : 'adr_street',
        'str_name' : feature['properties']['name'],
        'str_type' : feature['properties']['type'],
        'stl_name' : feature['properties']['settlement'],
        'stl_type' : feature['properties']['settlement_type'],
        'stl_id' : feature['properties']['settlement_id'],
        'dist_meters' : feature['properties']['dist_meters']
    }

    try:
        res['geometry'] = feature['geometry']
    except:
        pass
    return res

def parse_stl(feature):
    """
    returns dict
    'id', 'category' - required keys
    'dist_meters' - distance from point in search
    """
    res = {
        'id' : feature['id'],
        'category' : 'adm_settlement',
        'stl_name' : feature['properties']['name'],
        'stl_type' : feature['properties']['type'],
        'dist_meters' : feature['properties']['dist_meters']
    }

    try:
        res['adm1_name'] = feature['properties']['level1']
        res['adm1_id'] = feature['properties']['level1_id']
    except:
        pass

    try:
        res['adm2_name'] = feature['properties']['level2']
        res['adm2_id'] = feature['properties']['level2_id']
    except:
        pass

    try:
        res['geometry'] = feature['geometry']
    except:
        pass
    return res

def parse_dst(feature):
    """
    returns dict
    'id', 'category' - required keys
    'dist_meters' - distance from point in search
    """
    res = {
        'id' : feature['id'],
        'category' : 'adm_district',
        'dst_name' : feature['properties']['name'],
        'dst_type' : feature['properties']['type'],
        'stl_name' : feature['properties']['settlement'],
        'stl_type' : feature['properties']['settlement_type'],
        'stl_id' : feature['properties']['settlement_id'],
        'dist_meters' : feature['properties']['dist_meters']
    }

    try:
        res['geometry'] = feature['geometry']
    except:
        pass
    return res

def parse_adm1(feature):
    """
    returns dict
    'id', 'category' - required keys
    'dist_meters' - distance from point in search
    """
    res = {
        'id' : feature['id'],
        'category' : 'adm_level1',
        'adm1_name' : feature['properties']['name'],
        'admin_center_name' : feature['properties']['admin_center'],
        'admin_center_id' : feature['properties']['admin_center_id'],
        'dist_meters' : feature['properties']['dist_meters']
    }

    try:
        res['geometry'] = feature['geometry']
    except:
        pass
    return res

def parse_adm2(feature):
    """
    returns dict
    'id', 'category' - required keys
    'dist_meters' - distance from point in search
    """
    res = {
        'id' : feature['id'],
        'category' : 'adm_level2',
        'adm1_name' : feature['properties']['level1'],
        'adm1_id' : feature['properties']['level1_id'],
        'adm2_name' : feature['properties']['name'],
        # 'admin_center_name' : feature['properties']['admin_center'],
        # 'admin_center_id' : feature['properties']['admin_center_id'],
        'dist_meters' : feature['properties']['dist_meters']
    }

    try:
        res['geometry'] = feature['geometry']
    except:
        pass
    return res

def parse_cnt(feature):
    """
    returns dict
    'id', 'category' - required keys
    'dist_meters' - distance from point in search
    """
    res = {
        'id' : feature['id'],
        'category' : 'adm_country',
        'cnt_name' : feature['properties']['name'],
        'admin_center_name' : feature['properties']['admin_center'],
        'admin_center_id' : feature['properties']['admin_center_id'],
        'dist_meters' : feature['properties']['dist_meters']
    }

    try:
        res['geometry'] = feature['geometry']
    except:
        pass
    return res

def geocoded_object(parsed_features):
    '''
    this function pops features from parsed features and 
    combine into one nice geocoded dictionary object.
    full_string returns nice formated string
    '''
    res = {'full_string' : ''}
    categories = ('adr_address', 'adr_street', 'adm_settlement', 'adm_level2', 'adm_level1', 'adm_country')
    keys = ('id', 'adr_name', 'str_name', 'str_type', 'stl_name', 'stl_type', 'adm2_name', 'adm1_name', 'cnt_name')

    for category in categories:
        # getting features of category
        only_category = list(a for a in parsed_features if a['category'] == category)
        if only_category:
            # if more then one, getting the closest by dist_meters
            closest = sorted(only_category, key = lambda item: item['dist_meters'])[0]
            for k,v in closest.items():
                # adding required keys/values
                if k in keys and k not in res:
                    res[k] = v
    
    if 'adr_name' in res:
        res['full_string'] = f'{res["adr_name"]}'

    if 'str_name' in res and 'str_type' in res:
        if res['full_string'] != '':
            res['full_string'] = f'{res["str_type"]} {res["str_name"]}, {res["full_string"]}'
        else:
            res['full_string'] = f'{res["str_type"]} {res["str_name"]}'

    if 'stl_name' in res and 'stl_type' in res:
        if res['full_string'] != '':
            res['full_string'] = f'{res["stl_type"]} {res["stl_name"]}, {res["full_string"]}'
        else:
            res['full_string'] = f'{res["stl_type"]} {res["stl_name"]}'

    if 'adm2_name' in res:
        if res['full_string'] != '':
            res['full_string'] = f'{res["adm2_name"]}, {res["full_string"]}'
        else:
            res['full_string'] = f'{res["adm2_name"]}'

    if 'adm1_name' in res:
        if res['full_string'] != '':
            res['full_string'] = f'{res["adm1_name"]}, {res["full_string"]}'
        else:
            res['full_string'] = f'{res["adm1_name"]}'

    if 'cnt_name' in res:
        if res['full_string'] != '':
            res['full_string'] = f'{res["cnt_name"]}, {res["full_string"]}'
        else:
            res['full_string'] = f'{res["cnt_name"]}'
    
    return res