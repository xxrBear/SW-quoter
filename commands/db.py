import click

from db.setup import clear_table, delete_row, drop_db, init_db, reset_row, show_db


@click.group(name="db")
def cli_db():
    """执行数据库操作"""
    pass


@cli_db.command("init")
def init():
    """初始化数据库表"""
    init_db()


@cli_db.command("show")
def show():
    """展示数据库信息"""
    doc = show_db()
    click.secho(doc)


@cli_db.command("drop")
def drop():
    """删除数据库表结构"""
    confirm = click.confirm("确定要删除所有数据库表？此操作不可恢复！")
    if not confirm:
        click.secho("操作取消", fg="yellow")
    else:
        drop_db()
        click.secho("操作完成", fg="green")


@cli_db.command("clear")
def clear():
    """清空数据表所有数据"""
    confirm = click.confirm("确定要删除所有数据表记录？此操作不可恢复！")
    if not confirm:
        click.secho("操作取消", fg="yellow")
    else:
        count = clear_table()
        click.secho(f"已删除所有数据表记录共{count}条", fg="green")


@cli_db.command("delete")
@click.argument("days", type=click.IntRange(1, None))
def delete(days):
    """删除指定天数前的数据库表记录"""
    confirm = click.confirm(f"确定要删除{days}天前的所有数据表记录？此操作不可恢复！")
    if not confirm:
        click.secho("操作取消", fg="yellow")
    else:
        count = delete_row(days)
        click.secho(f"已删除{days}天前的数据共{count}条", fg="green")


@cli_db.command("reset")
@click.argument("_id", type=click.IntRange(1, None))
def reset(_id):
    """重置指定ID的数据库状态"""
    confirm = click.confirm(f"确定要重置ID为 {_id} 的数据")
    if not confirm:
        click.secho("操作取消", fg="yellow")
    else:
        reset_row(_id)
        click.secho("重置成功", fg="green")
