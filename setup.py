from setuptools import setup


setup(
    name='cldfbench_cathcart_et_al2020',
    py_modules=['cldfbench_cathcart_et_al2020'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'cldfbench.dataset': [
            'cathcart_et_al2020=cldfbench_cathcart_et_al2020:Dataset',
        ]
    },
    install_requires=[
        'phlorest',
    ],
    extras_require={
        'test': [
            'pytest-cldf',
        ],
    },
)
