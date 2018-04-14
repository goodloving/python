import matplotlib.pyplot as plo
import pygal
import json

def get_json(sfile = '2018-4-11.json'):
    with open(sfile, 'r', encoding='utf-8') as f:
        whether_dict = json.load(f)
    return whether_dict

def get_city(whether_dict):
    city_list = []
    for city in whether_dict:
        city_list.append(city)
    return city_list

def get_hightem(whether_dict):
    high_list = []
    for city in whether_dict:
        if whether_dict[city] != '无数据':
            high = whether_dict[city]['high']
            high_list.append(int(high[3:len(high)-1]))
        else:
            high_list.append(0)
    return high_list

def get_lowtem(whether_dict):
    low_list = []
    for city in whether_dict:
        if whether_dict[city] != '无数据':
            low = whether_dict[city]['low']
            low_list.append(int(low[3:len(low)-1]))
        else:
            low_list.append(0)
    return low_list

def use_matplotlib_pyplot():
    whether = get_json()
    x = get_city(whether)
    y_h = get_hightem(whether)
    y_l = get_lowtem(whether)
    fig = plo.figure(dpi=128, figsize=(10, 6))
    plo.plot(x, y_h, linewidth=1, c='red')
    plo.plot(x, y_l, linewidth=1, c='blue')
    plo.fill_between(x, y_h, y_l, facecolor='green', alpha=0.2)
    plo.title('日温度值域图', fontsize=15)
    plo.xlabel('城市', fontsize=10)
    plo.ylabel('温度', fontsize=10)
    plo.tick_params(axis='both', which='major', labelsize=1)
    fig.autofmt_xdate()
    plo.savefig('high-low.png', bbox='tight')
    plo.show()

def use_matplotlib_scatter():
    whether = get_json()
    x = get_city(whether)
    y_h = get_hightem(whether)
    y_l = get_lowtem(whether)
    fig = plo.figure(dpi=128, figsize=(10, 6))
    plo.scatter(x, y_h, s=1, c=y_h, cmap=plo.cm.Reds, edgecolors='none')
    plo.scatter(x, y_l, s=1, c=y_l, cmap=plo.cm.Blues, edgecolors='none')
    #plo.fill_between(x, y_h, y_l, facecolor='green', alpha=0.2)
    plo.title('日温度值域图', fontsize=15)
    plo.xlabel('城市', fontsize=10)
    plo.ylabel('温度', fontsize=10)
    plo.tick_params(axis='both', which='major', labelsize=1)
    fig.autofmt_xdate()
    plo.savefig('high-low-scatter.png', bbox='tight')
    plo.show()

def use_pygal():
    whether = get_json()
    x = get_city(whether)
    y_h = get_hightem(whether)
    y_l = get_lowtem(whether)
    hist = pygal.Bar()
    hist.title = 'the changes of everyday’temperature'
    hist.x_labels = x
    hist.x_title = 'city name'
    hist.y_title = 'temperature'
    hist.add('高温', y_h, c='red')
    hist.add('低温', y_l, c='blue')
    hist.render_to_file('high-low.svg')

def use_pygal_map():
    whether = get_json()
    x = get_city(whether)
    y_h = get_hightem(whether)
    y_l = get_lowtem(whether)
    cm = pygal.maps.world.World()
    cm.title = 'the changes of everyday’temperature'
    cm.add('high', y_h)
    cm.render_to_file('high-low-map.svg')

if __name__ == '__main__':
    use_matplotlib_pyplot()
    #use_pygal()
    #use_pygal_map()
    #use_matplotlib_scatter()
