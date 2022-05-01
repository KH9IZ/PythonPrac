def task_translation():
    """Update and compile translation"""
    domain = "prog"
    return {
        'actions': [f"pybabel extract --output-file={domain}.pot --input-dirs={domain}.py",
                    f"pybabel update --domain={domain} --input-file={domain}.pot --output-dir=po --locale=ru",
                    f"pybabel compile --domain={domain} --directory=po --locale=ru"],
        'targets': [f'{domain}.pot', f'po/ru/LC_MESSAGES/{domain}.mo'],
        'file_dep': [f"{domain}.py"],
        'clean': True
    }

def task_test():
    """Run test suit"""
    return {
        'actions': ["python3 -m unittest discover"],
        'file_dep': ['prog.py', 'test_prog.py']
    }

def task_wheel():
    """Build a wheel for prog"""
    import build
    return {
        'actions': ['python -m build -w'],
        'file_dep': ['prog.py', 'po/ru/LC_MESSAGES/prog.mo'],
        'targets': ['dist/prog-0.0.1-py3-none-any.whl']
    }


def task_sdist():
    """Build a cdist for prog"""
    import build
    return {
        'actions': ['python -m build -s'],
        'file_dep': ['prog.py', 'po/ru/LC_MESSAGES/prog.mo'],
        'targets': ['dist/prog-0.0.1.tar.gz']
    }
