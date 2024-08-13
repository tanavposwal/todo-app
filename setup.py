from setuptools import setup

setup(
    name='todo-app',
    version='1.0',
    py_modules=['app'],  # Replace 'your_script' with the name of your Python file without the '.py' extension
    entry_points='''
        [console_scripts]
        task-cli=your_script:main
    ''',
)
