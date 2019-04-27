from flask import Flask, render_template, request
from forms import GroupForm
from flask_wtf import csrf
from vk_function import get_data
from get_name import get_name
from dates_for_graph import dates_for_graph
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

@app.route('/results', methods=['POST'])
def results_page():
    vk_page = request.form['vk_group']
    title = 'Результаты:'
    results = str(get_data(vk_page))
    name = get_name(vk_page)
    graph = dates_for_graph(vk_page)
    labels = list(graph.keys())
    values = list(graph.values())
    max_posts = max(graph.items(), key=lambda k: k[1])
    year = max_posts[0]
    count = max_posts[1]
    a = str(f'Максимальное количество постов было в {year} году: {count}')

    return render_template('results.html', the_title=title, the_result=results, name=name, graph=graph, labels=labels, values=values, a=a)

@app.route('/')
def get_group_data():
    group_form = GroupForm()
    return render_template('group_link.html', form=group_form)

# @app.route('/')
# def start():
#     return render_template('test.html')

# @app.route('/results', methods=['POST'])
# def do_function():
#     result = request.form['url']
#     return str(count_letters(result))

app.run(debug=True)


