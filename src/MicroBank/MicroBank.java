// this file is java for jshell

// read the input data from the file
// each line looks like: 1/10/2026, deposit, 100.00

import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;

class MicroBank {
    // input file is "input.data"
    double balance = 0.0;
class Transaction {
    String date;
    String type;
    double amount;

    public Transaction(String date, String type, double amount) {
        this.date = date;
        this.type = type;
        this.amount = amount;
    }

    public double getAmount() {
        return this.amount;
    }
}

    public static void main(String[] args) {
        MicroBank mb = new MicroBank();
        ArrayList<Transaction> xactions = mb.readData("input.data");
        for (Transaction t : xactions) {
            if (t.type.equals("withdrawal")) {
                mb.balance -= t.amount;
            } else if (t.type.equals("deposit")) {
                mb.balance += t.amount;
            }
        }
        System.out.println(String.format("Final Balance: $%.2f", mb.balance));
    }

    ArrayList<Transaction> readData(String filename) {
        ArrayList<Transaction> list = new ArrayList<>();
        // open a text file and read each line, putting the fields into a Transaction object.
        try {
            Files.lines(Paths.get(filename))
                .forEach(line -> {
                    String[] parts = line.split(", ");
                    if (parts.length == 3) {
                        list.add(new Transaction(parts[0], parts[1], Double.parseDouble(parts[2])));
                    }
                });
        } catch (java.io.IOException e) {
            e.printStackTrace();
        }
        return list;
    }
}
