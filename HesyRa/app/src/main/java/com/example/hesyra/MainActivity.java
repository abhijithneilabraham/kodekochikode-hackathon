package com.example.hesyra;

import android.content.ContentValues;
import android.content.Intent;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    SQLiteOpenHelper openHelper;
    SQLiteDatabase db;
    Button _reg, _log;
    EditText _fname, _lname, _mail, _phoneno, _pword, _idno;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        openHelper=new DatabaseHelper(this);
        _reg=(Button)findViewById(R.id.reg);
        _log=(Button)findViewById(R.id.log);
        _fname=(EditText)findViewById(R.id.fname);
        _lname=(EditText)findViewById(R.id.lname);
        _mail=(EditText)findViewById(R.id.mail);
        _phoneno=(EditText)findViewById(R.id.phoneno);
        _pword=(EditText)findViewById(R.id.pword);
        _idno=(EditText)findViewById(R.id.idno);
        _reg.setOnClickListener(new OnClickListener() {
            @Override
            public void onClick(View v) {
                db=openHelper.getWritableDatabase();
                String fname1=_fname.getText().toString();
                String lname1=_lname.getText().toString();
                String idno1=_idno.getText().toString();
                String mail1=_mail.getText().toString();
                String pword1=_pword.getText().toString();
                String phoneno1=_phoneno.getText().toString();
                insertdata(fname1, lname1, idno1, mail1, pword1, phoneno1);
                Toast.makeText(getApplicationContext(), "Registered successfully!", Toast.LENGTH_LONG).show();
            }
        });
        _log.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(MainActivity.this, login.class);
                startActivity(intent);
            }
        });
    }
    public void insertdata (String fname1, String lname1, String idno1, String mail1, String pword1, String phoneno1) {
        ContentValues contentValues= new ContentValues();
        contentValues.put(DatabaseHelper.COL_2, fname1);
        contentValues.put(DatabaseHelper.COL_3, lname1);
        contentValues.put(DatabaseHelper.COL_1, idno1);
        contentValues.put(DatabaseHelper.COL_4, mail1);
        contentValues.put(DatabaseHelper.COL_5, pword1);
        contentValues.put(DatabaseHelper.COL_6, phoneno1);
        long id= db.insert(DatabaseHelper.TABLE_NAME, null, contentValues);
    }
}
