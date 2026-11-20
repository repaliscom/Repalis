import os
import re

def replace_in_file(path, replacements):
    if not os.path.exists(path):
        return 0
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
    except (UnicodeDecodeError, PermissionError):
        return 0
    orig = content
    for pattern, repl in replacements:
        if isinstance(pattern, str):
            content = content.replace(pattern, repl)
        else:
            content = pattern.sub(repl, content)
    if content != orig:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        return 1
    return 0

replace_in_file('server/repalis/account/service.py', [
    ('main Polar currency', 'main Repalis currency'),
])

replace_in_file('server/repalis/agent/identity_assertion.py', [
    ('JWT Polar signs', 'JWT Repalis signs'),
    ('polar.kit.jwt', 'repalis.kit.jwt'),
])

replace_in_file('server/repalis/app.py', [
    ('polar_frontend_matcher', 'repalis_frontend_matcher'),
    ('polar_frontend_config', 'repalis_frontend_config'),
])

replace_in_file('server/repalis/auth/endpoints.py', [
    ('"Polar" if settings.is_production() else f"Polar {settings.ENV.value.capitalize()}"',
     '"Repalis" if settings.is_production() else f"Repalis {settings.ENV.value.capitalize()}"'),
    (re.compile(r'\bPolar\b'), 'Repalis'),
])

replace_in_file('server/repalis/auth/schemas.py', [
    ('polar_last_login_method', 'repalis_last_login_method'),
])

replace_in_file('server/repalis/backoffice/__init__.py', [
    ('aria_label="Polar"', 'aria_label="Repalis"'),
    ('Polar Backoffice', 'Repalis Backoffice'),
])

replace_in_file('server/repalis/backoffice/components/_base.py', [
    ('Polar Backoffice', 'Repalis Backoffice'),
])

replace_in_file('server/migrations/script.py.mako', [
    ('# Polar Custom Imports', '# Repalis Custom Imports'),
])

replace_in_file('server/load_tests/common/test_data.py', [
    ('polar_oat_*', 'repalis_oat_*'),
])
replace_in_file('server/load_tests/config.py', [
    ('polar_oat_*', 'repalis_oat_*'),
])

replace_in_file('server/monitoring/grafana/provisioning/dashboards/dashboards.yml', [
    ('Polar Dashboards', 'Repalis Dashboards'),
])

for root, _, files in os.walk('server/monitoring/grafana/dashboards'):
    for f in files:
        p = os.path.join(root, f)
        replace_in_file(p, [
            ('"name": "polar-', '"name": "repalis-'),
            ('"uid": "polar-', '"uid": "repalis-'),
            ('"tags": ["polar"', '"tags": ["repalis"'),
            ('"polar"', '"repalis"'),
            ('polarsh', 'repalis'),
        ])

for b in ['server/benchmarks/test_event.py', 'server/benchmarks/test_outpost.py']:
    replace_in_file(b, [
        (re.compile(r'\bPolar\b'), 'Repalis'),
        ("Polar's", "Repalis's"),
    ])

print("Server Part 5 execution complete.")
