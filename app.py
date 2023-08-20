# Import libraries
from flask import Flask, redirect, request, render_template, url_for
# Instantiate Flask functionality
app = Flask(__name__)
# Sample data
transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': -200},
    {'id': 3, 'date': '2023-06-03', 'amount': 300}
]


@app.route("/")
def get_transactions():
    return render_template("transactions.html", transactions=transactions)


@app.route('/add', methods=['GET', 'POST'])
def add_transaction():
    if request.method == 'POST':
        id_ = len(transactions) + 1
        date = request.form.get('date')
        amount = float(request.form.get('amount'))
        transactions.append({'id': id_, 'date': date, 'amount': amount})
        return redirect(url_for('get_transactions'))
    return render_template('form.html')


@app.route('/edit/<int:transaction_id>', methods=['GET', 'POST'])
def edit_transaction(transaction_id):
    if request.method == 'POST':
        id_ = -1
        for i, _ in enumerate(transactions):
            if transactions[i].get('id') == transaction_id:
                id_ = i
                break
        if i != -1:
            transaction = {
                'id': id_,
                'date': request.form.get('date'),
                'amount': float(request.form.get('amount'))
            }
            transactions[i] = transaction
            return redirect(url_for('get_transactions'))
        return {'message': 'ID not found'}, 404
    # return render_template('edit.html', transaction=transaction)
    for transaction in transactions:
        if transaction['id'] == transaction_id:
            return render_template("edit.html", transaction=transaction)


@app.route('/delete/<int:transaction_id>', methods=['GET'])
def delete_transaction(transaction_id):
    id_ = -1
    for i, _ in enumerate(transactions):
        if transactions[i].get('id') == transaction_id:
            id_ = i
            break
    if i != -1:
        del transactions[id_]
        return redirect(url_for('get_transactions'))
    return {'message': 'ID not found'}, 404


if __name__ == "__main__":
    app.run(debug=True)
