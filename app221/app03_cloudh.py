#!/usr/bin/env python
# -*- coding: utf8 -*-
# 			app03_cloudh.py
#
#   https://github.com/BestJudy/chess
#
import json
import numpy as np
from urllib import request, parse
from urllib.error import URLError, HTTPError
import time

def app221Login(username, password=''):
    ret = 0
    # Making a GET request
    urlData = 'http://cloudh.org/house_app/login.php?'+'&username='+username+'&password='+password

    try:
        webURL = request.urlopen(urlData)  
        data = webURL.read()
        # print(data)
        encoding = webURL.info().get_content_charset('utf-8')
        JSON_object = json.loads(data.decode(encoding))
        ret = int(JSON_object['param10_ret'])
    except Exception:
        print('app221Login error')
    return ret
#ret =  app221Login('bestjudyw@gmail.com', 'zzy403')
#print( 'app221Login', ret )
def app221GetGameData(id_game, h_player=''):
    ret_arr = np.array([0])
    turn_now = 1
    # Making a GET request
    urlData = 'http://cloudh.org/house_app/app221/h_app_list_all.php?'+'&query_h_id='+str(id_game)+'&h_player1='+h_player

    try:
        webURL = request.urlopen(urlData)  
        data = webURL.read()
        #print('  app221GetGameData', data)
        encoding = webURL.info().get_content_charset('utf-8')
        JSON_object = json.loads(data.decode(encoding))
        ret = JSON_object[0]['h_data1']
        ret = ret.replace('[', '').replace(']', '')
        ret_arr = np.fromstring(ret, dtype=int, sep=' ')
        if(len(ret_arr) >= 64): #ret_arr = np.zeros((8, 8))
            ret_arr.shape = (8, 8)
        turn_now = int(JSON_object[0]['h_turn2'])
    except Exception:
        print('app221GetGameData error')
    return (ret_arr, turn_now)
#arr_ret = app221GetGameData('lunawyh@gmail.com')
#arr_ret = app221GetGameData(4)
#print(arr_ret)

def app20SaveGameData(h_house_i, _data_url):
    ret = 0
    
    #data_dict = 'query_h_id=' + query_h_id + '&h_house_item=' + h_house_i
    data_in = parse.urlencode(h_house_i).encode()
    try:
        req =  request.Request(_data_url, data=data_in) # this will make the method "POST"
        webURL = request.urlopen(req)
        data_out = webURL.read()
        #print(data_out)
        encoding = webURL.info().get_content_charset('utf-8')
        JSON_object = json.loads(data_out.decode(encoding))
        print('app20SaveGameData', JSON_object)
        return 200, JSON_object
    except HTTPError as e:
        # do something
        print('Error code: ', e.code)
    except URLError as e:
        # do something
        print('Reason: ', e.reason)
    except Exception:
        print('app20SaveGameData error')
    return ret, ""
def app20SaveGame(id_game, data_game, role_cur=2):
    if(id_game <= 0): return
    data_dictionary = {'h_id': 0, 
                    't_updated':0, 
                    'h_player1': '',
                    'h_player2': '',
                    'h_turn1': 0,
                    'h_turn2': 0,
                    'h_data1': '[0,0]',
                    'h_note': 'happy'
                    }
    data_dictionary['h_id'] = id_game
    data_dictionary['t_updated'] = time.time()
    data_dictionary['h_data1'] = data_game
    data_dictionary['h_turn1'] = role_cur
    data_dictionary['h_turn2'] = 3 - role_cur
    data_jsonString = json.dumps(data_dictionary)
    post_dictionary = {'query_h_id':200, 'h_app_item':'data'}
    post_dictionary['h_app_item'] = data_jsonString
    data_url = 'http://cloudh.org/house_app/app221/h_app_manage.php'
    app20SaveGameData(post_dictionary, data_url)

def app20SetUser(p_name, role_cur=2, state_cur=0):
    print('  app20SetUser', p_name, role_cur, state_cur)
    data_dictionary = {'h_id': 0, 
                    't_updated':0, 
                    'h_name': '',
                    'h_role': 0,
                    'h_state': 0,
                    'h_room': 0,
                    'h_note': 'smart'
                    }
    data_dictionary['h_id'] = 0
    data_dictionary['t_updated'] = time.time()
    data_dictionary['h_name'] = p_name
    data_dictionary['h_role'] = role_cur
    data_dictionary['h_state'] = state_cur
    data_jsonString = json.dumps(data_dictionary)
    post_dictionary = {'query_h_id':0, 'h_app_item':'data'}
    post_dictionary['h_app_item'] = data_jsonString
    data_url = 'http://cloudh.org/house_app/app221/h_app_man_user.php'
    ret, ret_json = app20SaveGameData(post_dictionary, data_url)
    if(ret == 200):
        return ret_json[0]['h_id']
    else:
        return 0
def app20getPartner(id_user, role_cur=2, n_ignore=0):
    if(id_user < 0):
        return 0, ''
    print('  app20getPartner', id_user, role_cur, n_ignore)
    data_dictionary = {'h_id': 0, 
                    't_updated':0, 
                    'h_name': '',
                    'h_role': 0,
                    'h_state': 0,
                    'h_room': 0,
                    'h_note': 'smart'
                    }
    data_dictionary['h_id'] = id_user
    data_dictionary['t_updated'] = time.time()
    data_dictionary['h_name'] = 'not set'
    data_dictionary['h_role'] = role_cur
    data_dictionary['h_state'] = n_ignore
    data_jsonString = json.dumps(data_dictionary)
    post_dictionary = {'query_h_id':200, 'h_app_item':'data'}
    post_dictionary['h_app_item'] = data_jsonString
    data_url = 'http://cloudh.org/house_app/app221/h_app_man_user.php'
    ret, ret_json = app20SaveGameData(post_dictionary, data_url)
    if(ret == 200):
        return ret_json[0]['h_room'], ret_json[0]['h_name']
    else:
        return 0, ''
def app20UpdateUser(id_user, name_user, role_cur, state_cur, room_cur):
    print('  app20UpdateUser', id_user, name_user, role_cur, state_cur, room_cur)
    data_dictionary = {'h_id': 0, 
                    't_updated':0, 
                    'h_name': '',
                    'h_role': 0,
                    'h_state': 0,
                    'h_room': 0,
                    'h_note': 'smart'
                    }
    data_dictionary['h_id'] = id_user
    data_dictionary['t_updated'] = time.time()
    data_dictionary['h_name'] = name_user
    data_dictionary['h_role'] = role_cur
    data_dictionary['h_state'] = state_cur
    data_dictionary['h_room'] = room_cur
    data_jsonString = json.dumps(data_dictionary)
    post_dictionary = {'query_h_id':300, 'h_app_item':'data'}
    post_dictionary['h_app_item'] = data_jsonString
    data_url = 'http://cloudh.org/house_app/app221/h_app_man_user.php'
    ret, ret_json = app20SaveGameData(post_dictionary, data_url)
    if(ret == 200):
        return ret_json[0]['h_room'], ret_json[0]['h_name']
    else:
        return 0, ''