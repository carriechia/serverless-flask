import datetime
import pytz
from croniter import croniter

from utils.database import db
from services.jobs import check_and_run_job
from utils.sqs import push_sqs
from utils.database import connect_db



def cron_job(event, context):
    data = []
    now = datetime.datetime.now()
    tw = pytz.timezone('Asia/Taipei')
    now_datetime = tw.localize(now).replace(microsecond=0)

    job_list = Jobs.query.filter(Jobs.status == 1).all()
    for job in job_list:
        valid = croniter.is_valid(job.cron)
        if not valid:
            raise Exception('')

        match_job = croniter.match(job.cron, now_datetime)
        if match_job is True:
            data.append({'func_name': job.func_name, 'params': job.params})
    push_sqs(data)