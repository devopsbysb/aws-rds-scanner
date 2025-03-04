import boto3
import json
import argparse

def get_rds_instances(region):
    """Retrieve metadata of all AWS RDS instances in the given region."""
    rds_client = boto3.client('rds', region_name=ap-south-1)

    try:
        # Fetch all RDS instances
        response = rds_client.describe_db_instances()
        instances = response.get('DBInstances', [])

        # Extract required metadata
        rds_data = []
        for instance in instances:
            rds_data.append({
                'DBInstanceIdentifier': instance['DBInstanceIdentifier'],
                'Engine': instance['Engine'],
                'Status': instance['DBInstanceStatus'],
                'Endpoint': instance['Endpoint']['Address'] if 'Endpoint' in instance else 'N/A'
            })

        # Return JSON formatted output
        return json.dumps(rds_data, indent=4)

    except Exception as e:
        return json.dumps({"error": str(e)}, indent=4)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AWS RDS Instance Scanner")
    parser.add_argument("--region", required=True, help="AWS region to scan")
    args = parser.parse_args()

    print(get_rds_instances(args.region))

