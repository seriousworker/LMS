def qs2html(ql_list):
    s = '<table>'

    for record in ql_list:
        s += f'<tr><td>{record.first_name}</td>' \
             f'<td>{record.last_name}</td>' \
             f'<td>{record.email}</td>' \
             f'</tr>'

    s += '</table>'

    return s
