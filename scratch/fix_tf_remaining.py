with open('terraform/modules/aws_task_worker/variables.tf', 'r', encoding='utf-8') as f:
    text = f.read().replace('polar-{environment}-worker-{name}', 'repalis-{environment}-worker-{name}')
with open('terraform/modules/aws_task_worker/variables.tf', 'w', encoding='utf-8') as f:
    f.write(text)

with open('terraform/modules/ecs_service/variables.tf', 'r', encoding='utf-8') as f:
    text = f.read().replace('polar-{environment}-{name}', 'repalis-{environment}-{name}')
with open('terraform/modules/ecs_service/variables.tf', 'w', encoding='utf-8') as f:
    f.write(text)

with open('terraform/modules/render_service/backoffice.tf', 'r', encoding='utf-8') as f:
    text = f.read().replace('polar-backoffice-', 'repalis-backoffice-')
with open('terraform/modules/render_service/backoffice.tf', 'w', encoding='utf-8') as f:
    f.write(text)

with open('terraform/modules/s3_buckets/main.tf', 'r', encoding='utf-8') as f:
    text = f.read().replace('polar-{environment}-*', 'repalis-{environment}-*')
    text = text.replace('? "polar"', '? "repalis"')
with open('terraform/modules/s3_buckets/main.tf', 'w', encoding='utf-8') as f:
    f.write(text)

with open('terraform/sandbox/render.tf', 'r', encoding='utf-8') as f:
    text = f.read().replace('workspace    = "polar"', 'workspace    = "repalis"')
with open('terraform/sandbox/render.tf', 'w', encoding='utf-8') as f:
    f.write(text)

with open('terraform/test/render.tf', 'r', encoding='utf-8') as f:
    text = f.read().replace('workspace    = "polar"', 'workspace    = "repalis"')
with open('terraform/test/render.tf', 'w', encoding='utf-8') as f:
    f.write(text)

print('All 8 non-POLAR matches updated successfully.')
