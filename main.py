import os
from pathlib import Path
import subprocess

def main():
    input_dir = Path(os.environ['INPUT_DIR'])
    output_dir = Path(os.environ['OUTPUT_DIR'])

    print(f"Input dir: {input_dir}")
    print(f"Output dir: {output_dir}")

    output_dir.mkdir(parents=True, exist_ok=True)

    fastq_files = list(input_dir.glob("*.fastq")) + list(input_dir.glob("*.fastq.gz"))

    if not fastq_files:
        print("No FASTQ files found in input directory!")
        return

    print(f"Found {len(fastq_files)} FASTQ files.")

    for f in fastq_files:
        print(f"Running FastQC on {f.name}")
        subprocess.run(["fastqc", str(f), "--outdir", str(output_dir)], check=True)

    print("FastQC analysis completed.")

if __name__ == "__main__":
    main()

