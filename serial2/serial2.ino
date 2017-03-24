#include <MsTimer2.h>

#define echoPin 10 // Echo Pin
#define trigPin 9 // Trigger Pin
#define powerPin 7 // Power Pin

double Duration = 0; //受信した間隔
double Distance = 0; //距離

// 割り込み時に処理される関数
void flash() {
  digitalWrite( powerPin, LOW );
  delay(100000);
  digitalWrite( powerPin, HIGH );
}

void setup() {
Serial.begin( 9600 );
pinMode( echoPin, INPUT );
pinMode( trigPin, OUTPUT );
pinMode( powerPin, OUTPUT );
MsTimer2::set(2000, flash);     // 2s毎にflash( )割込み関数を呼び出す様に設定
}

void loop() {
  //電源オン
  digitalWrite( powerPin, HIGH );
  //Triger
  digitalWrite(trigPin, LOW); 
  delayMicroseconds(2); 
  digitalWrite( trigPin, HIGH ); //トリガ出力
  delayMicroseconds( 10 );       //トリガ10us
  digitalWrite( trigPin, LOW );
  // Echo
  Duration = pulseIn( echoPin, HIGH ); //センサからの入力
  if (Duration > 0) {
    MsTimer2::start();             // タイマー割り込み開始
    Duration = Duration/2; //往復距離を半分にする
    // 音速340m/s 100 1000000us=1s で計算（温度補正なし）
    Distance = Duration*340*100/1000000;
    Serial.println(Distance);
  }
  delay(500);
}



