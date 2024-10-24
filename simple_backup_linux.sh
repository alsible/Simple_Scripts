#!/bin/bash
SOURCE_DIR="<insert_source_folder_here>"
BACKUP_DIR="/opt/backup/"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
BACKUP_FILE="$BACKUP_DIR/backup_$TIMESTAMP.tar.gz"
LOG_FILE="/opt/backup/backup.log"

# Create backup and log the process
{
    echo "[$(date)] Starting backup of $SOURCE_DIR"
    tar -czf $BACKUP_FILE $SOURCE_DIR && echo "[$(date)] Backup successful: $BACKUP_FILE" || echo "[$(date)] Backup failed."
    find $BACKUP_DIR -type f -name "*.tar.gz" -mtime +7 -exec rm {} \; && echo "[$(date)] Old backups deleted." || echo "[$(date)] Failed to delete old backups."
} >> $LOG_FILE 2>&1
