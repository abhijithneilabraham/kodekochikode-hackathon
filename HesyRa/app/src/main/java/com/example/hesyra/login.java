package com.example.hesyra;

import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

public class login extends AppCompatActivity {
    SQLiteDatabase db;
    SQLiteOpenHelper openHelper;
    Button _login;
    EditText _emaillogin, _pwordlogin;
    Cursor cursor;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);
        openHelper = new DatabaseHelper(this);
        db=openHelper.getReadableDatabase();
        _login=(Button)findViewById(R.id.login);
        _emaillogin=(EditText)findViewById(R.id.emaillogin);
        _pwordlogin=(EditText)findViewById(R.id.pwordlogin);
        _login.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String email2 = _emaillogin.getText().toString();
                String pword2 = _pwordlogin.getText().toString();
                cursor = db.rawQuery(" SELECT * FROM " + DatabaseHelper.TABLE_NAME + " WHERE " + DatabaseHelper.COL_4 + "=? AND " + DatabaseHelper.COL_5 + " =? ", new String[]{email2, pword2});
                if(cursor!=null){
                    if(cursor.getCount()>0){
                        cursor.moveToNext();
                        Toast.makeText(getApplicationContext(), "Logged in Successfully!" , Toast.LENGTH_LONG).show();
                    }
                    else
                        Toast.makeText(getApplicationContext(), "error", Toast.LENGTH_LONG).show();
                }
            }
        });
    }
}
