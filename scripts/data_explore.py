import os

import dotenv
import pandas as pd
import pylab as plt
from moonsense.client import Client

dotenv.load_dotenv()
client = Client(secret_token=os.environ['MOONSENSE_SECRET_TOKEN'])


def main():
    # get all the sessions we've recorded so far
    sessions = client.list_sessions()

    # filter the sessions to keep only the ones we've labeled with the tag "squats" from the app

    def filter_squat_session(labels):
        for label in labels:
            squats_mentioned = ['squats' in label]
        return any(squats_mentioned)

    sessions = [session for session in sessions if filter_squat_session(session.labels)]

    for session in sessions:

        session_acceleration_data = []
        session_gyro_data = []
        for payload in client.read_session(session_id=session.session_id):
            session_acceleration_data.extend(payload['bundle']['accelerometer_data'])
            session_gyro_data.extend(payload['bundle']['gyroscope_data'])

        df_acceleration = pd.DataFrame.from_records(session_acceleration_data)
        session_gyro_data = pd.DataFrame.from_records(session_gyro_data)
        if df_acceleration.empty:
            continue
        df_acceleration.rename(columns={'determined_at': 'timestamp'}, inplace=True)
        df_acceleration['timestamp'] = df_acceleration['timestamp'].astype(int)
        df_acceleration.sort_values(by='timestamp', inplace=True)
        # calculate time difference from session start in seconds
        df_acceleration['t'] = (df_acceleration['timestamp'] - df_acceleration['timestamp'].min()) / 1000

        df_acceleration.rename(columns={'determined_at': 'timestamp'}, inplace=True)
        df_acceleration['timestamp'] = df_acceleration['timestamp'].astype(int)
        df_acceleration.sort_values(by='timestamp', inplace=True)
        # calculate time difference from session start in seconds
        df_acceleration['t'] = (df_acceleration['timestamp'] - df_acceleration['timestamp'].min()) / 1000

        plt.figure(figsize=(8, 8))
        plt.plot(df_acceleration['t'], df_acceleration['x'], label='x')
        plt.plot(df_acceleration['t'], df_acceleration['y'], label='y')
        plt.plot(df_acceleration['t'], df_acceleration['z'], label='z')
        plt.legend()
        plt.title(' '.join(session.labels))
        plt.show()

    pass


if __name__ == '__main__':
    main()
