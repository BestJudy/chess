#!/usr/bin/env python
# -*- coding: utf8 -*-
# 			app03_cloudh.py
#
#   refer to: https://github.com/lincolnloop/python-qrcode
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
        print('error')
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
        #print(data)
        encoding = webURL.info().get_content_charset('utf-8')
        JSON_object = json.loads(data.decode(encoding))
        ret = JSON_object[0]['h_data1']
        ret = ret.replace('[', '').replace(']', '')
        ret_arr = np.fromstring(ret, dtype=int, sep=' ')
        if(len(ret_arr) >= 64): #ret_arr = np.zeros((8, 8))
            ret_arr.shape = (8, 8)
        turn_now = int(JSON_object[0]['h_turn2'])
    except Exception:
        print('error')
    return (ret_arr, turn_now)
#arr_ret = app221GetGameData('lunawyh@gmail.com')
#arr_ret = app221GetGameData(4)
#print(arr_ret)


def app221GetGameId(h_player='', _role=1):
    ret = (0, 0, '')
    # Making a GET request
    urlData = 'http://cloudh.org/house_app/app221/h_app_list_all.php?'+'&query_h_id='+'0'+'&h_player1='+h_player
    if(_role == 2):
        urlData = 'http://cloudh.org/house_app/app221/h_app_list_all.php?'+'&query_h_id='+'0'+'&h_player2='+h_player
    try:
        webURL = request.urlopen(urlData)  
        data = webURL.read()
        #print(data)
        encoding = webURL.info().get_content_charset('utf-8')
        JSON_object = json.loads(data.decode(encoding))
        role = 0
        h_player_other = ''
        if(JSON_object[0]['h_player1'] == h_player):
            role = 1
            h_player_other = JSON_object[0]['h_player2']
        if(JSON_object[0]['h_player2'] == h_player):
            role = 2
            h_player_other = JSON_object[0]['h_player1']
        ret = (int(JSON_object[0]['h_id']), role, h_player_other)
        
    except Exception:
        print('error')
    return ret
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
        #print('app20SaveGameData', JSON_object)
    except HTTPError as e:
        # do something
        print('Error code: ', e.code)
    except URLError as e:
        # do something
        print('Reason: ', e.reason)
    except Exception:
        print('error')
    return ret
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

def app20CreateGame(p_name, role_cur=2):
    #print('  app20CreateGame', p_name, role_cur)
    data_dictionary = {'h_id': 0, 
                    't_updated':0, 
                    'h_player1': '',
                    'h_player2': '',
                    'h_turn1': 0,
                    'h_turn2': 0,
                    'h_data1': '[0,0]',
                    'h_note': 'happy'
                    }
    data_dictionary['h_id'] = -10
    data_dictionary['t_updated'] = time.time()
    if(role_cur == 1):
        data_dictionary['h_player1'] = p_name
    elif(role_cur == 2):
        data_dictionary['h_player2'] = p_name
    data_dictionary['h_turn1'] = role_cur
    data_dictionary['h_turn2'] = 3 - role_cur
    data_jsonString = json.dumps(data_dictionary)
    post_dictionary = {'query_h_id':200, 'h_app_item':'data'}
    post_dictionary['h_app_item'] = data_jsonString
    data_url = 'http://cloudh.org/house_app/app221/h_app_man_player.php'
    app20SaveGameData(post_dictionary, data_url)
    pass