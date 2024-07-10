import sys
import psycopg2
from psycopg2 import sql
import time
from threading import Thread

import odom_structures

def setup_database(db):
    cur = db.cursor()
    cur.execute('''
        DROP TABLE IF EXISTS transactions;
    ''')
    cur.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id SERIAL PRIMARY KEY,
            seq INTEGER,
            secs INTEGER,
            nsecs INTEGER,
            frame_id TEXT,
            child_frame_id TEXT,
            position_x REAL,
            position_y REAL,
            position_z REAL,
            orientation_x REAL,
            orientation_y REAL,
            orientation_z REAL,
            orientation_w REAL,
            covariance TEXT,
            linear_x REAL,
            linear_y REAL,
            linear_z REAL,
            angular_x REAL,
            angular_y REAL,
            angular_z REAL,
            twist_covariance TEXT
        );
    ''')
    db.commit()
    cur.close()

def interact(db, odom):
    with db.cursor() as cur:
        sql_query = sql.SQL('''
            INSERT INTO transactions (
                seq, secs, nsecs, frame_id, child_frame_id, 
                position_x, position_y, position_z, 
                orientation_x, orientation_y, orientation_z, orientation_w,
                covariance, linear_x, linear_y, linear_z, 
                angular_x, angular_y, angular_z, twist_covariance
            ) VALUES (
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
            )
        ''')

        values = (
            odom.seq, odom.secs, odom.nsecs, odom.frame_id, odom.child_frame_id,
            odom.position_x, odom.position_y, odom.position_z,
            odom.orientation_x, odom.orientation_y, odom.orientation_z, odom.orientation_w,
            str(odom.covariance), odom.linear_x, odom.linear_y, odom.linear_z,
            odom.angular_x, odom.angular_y, odom.angular_z, str(odom.twist_covariance)
        )

        start = time.time()
        cur.execute(sql_query, values)
        db.commit()
        aux_time = time.time() - start

        print('Done! Time:', aux_time, 'seconds.')
        return aux_time

def sendTransactionsSimultaneously(db, odomData):
    threads = []
    times = []
    for odom in odomData:
        thread = Thread(target=lambda: times.append(interact(db, odom)))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    return times

def readOdomData(files):
    print('Reading files...')
    odomData = []
    for file in files:
        odomData.append(odom_structures.cleanPose(file))
    print('Done!')
    return list(zip(*odomData)) # Transposing

def writeTimesToFile(transactionTimes):
    print('Writing times...')
    transactionTimes = [list(column) for column in zip(*transactionTimes)]
    for i, times in enumerate(transactionTimes, start=1):
        with open(f'out_times{i}.txt', 'a') as f:
            for time in times:
                f.write(f'{time}\n')
    print('Done!')

def main():
    # Set this correctly
    db = psycopg2.connect(
        dbname='', 
        user='', 
        password='', 
        host='localhost', 
        port='5432'
    )
    
    setup_database(db)
    
    files = ['pose1.txt', 'pose2.txt', 'pose3.txt', 'pose4.txt']

    odomData = readOdomData(files)

    print(odomData)

    transactionTimes = []
    for i, odom in enumerate(odomData, start=1):
        print(f"Transaction number: {i}")
        transactionTimes.append(sendTransactionsSimultaneously(db, odom))
    
    writeTimesToFile(transactionTimes)
    
    db.close()

if __name__ == "__main__":
    main()