#!/usr/bin/env python3
import subprocess


def message(text):
    return print(f'{text}')


if __name__ == '__main__':
    message("\033[4m\033[1;36m\033[40m{}\033[0m".format("Удаление контейнеров"))
    delete_containers = subprocess.run(
        'docker-compose down -v',
        shell=True, encoding='utf-8', capture_output=True, cwd='/home/makarovskiynv@admlbt.rf/myStockroom'
    )
    if delete_containers.returncode == 0:
        message("\033[4m\033[1;32m\033[40m{}\033[0m".format("Контейнеры успешно остановлены"))
    else:
        message("\033[4m\033[1;31m\033[40m{}\033[0m".format(delete_containers.stderr))

    message("\033[4m\033[1;36m\033[40m{}\033[0m".format("Удаление базы данных"))
    delete_database = subprocess.run(
        'rm -Rfv database/pgdata',
        shell=True, encoding='utf-8', check=True, cwd='/home/makarovskiynv@admlbt.rf/myStockroom'
    )
    if delete_database.returncode == 0:
        message("\033[4m\033[1;32m\033[40m{}\033[0m".format("БД успешно удалена"))
    else:
        message("\033[4m\033[1;31m\033[40m{}\033[0m".format(delete_database.stderr))

    message("\033[4m\033[1;36m\033[40m{}\033[0m".format("Удаление docker образов"))
    delete_images = subprocess.run('docker rmi mystockroom-web:latest mystockroom-flower:latest mystockroom-celery:latest mystockroom-celery-beat:latest backend-nginx:latest redis:alpine postgres:14',
                                   shell=True, encoding='utf-8')
    if delete_images.returncode == 0:
        message("\033[4m\033[1;32m\033[40m{}\033[0m".format("Docker образы успешно удалены"))
    else:
        message("\033[4m\033[1;31m\033[40m{}\033[0m".format(delete_images.stderr))

    message("\033[4m\033[1;36m\033[40m{}\033[0m".format("Очистка мусора docker"))
    delete_system = subprocess.run(
        'docker system prune',
        shell=True, encoding='utf-8', check=True,
    )
    if delete_system.returncode == 0:
        message("\033[4m\033[1;32m\033[40m{}\033[0m".format("Мусор docker успешно удалены"))
    else:
        message("\033[4m\033[1;31m\033[40m{}\033[0m".format(delete_system.stderr))

    message("\033[4m\033[1;36m\033[40m{}\033[0m".format("Сборка контейнеров docker"))
    build_containers = subprocess.run(
        'docker-compose up -d --build',
        shell=True, encoding='utf-8', check=True, timeout=900, cwd='/home/makarovskiynv@admlbt.rf/myStockroom'
    )
    if build_containers.returncode == 0:
        message("\033[4m\033[1;32m\033[40m{}\033[0m".format("Контейнеры успешно собраны"))
    else:
        message("\033[4m\033[1;31m\033[40m{}\033[0m".format(build_containers.stderr))
